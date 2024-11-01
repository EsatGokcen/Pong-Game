import pygame
import random

class Paddle:
    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))

    def move(self,direction):
        if direction == 'up':
            self.y -= 5
        elif direction == 'down':
            self.y += 5


class Ball:
    
    def __init__(self,x,y,radius,color):
        self.x = 400
        self.y = 300
        self.radius = radius
        self.color = color
        self.x_vel = random.randint(-15,15)
        self.y_vel = random.randint(-15,15)
        if self.x_vel == 0 and self.y_vel == 0: #makes sure ball is always moving
            self.x_vel = 5 

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
    
    def move(self):
        self.x = self.x + self.x_vel
        self.y = self.y + self.y_vel


    def bounce(self):
        self.x_vel *= -1 #multiplying x coords with -1 will reverse their direction
        self.y_vel = random.randint(-5,5)

def main():
    pygame.init()

    #Display:
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption('Pong Game')

    #Game Objects:
    player_1 = Paddle(10,100,10,100,'red')
    player_2 = Paddle(WIDTH - 20,100,10,100,'blue')
    ball = Ball(WIDTH // 2, HEIGHT // 2, 10,'white')

    #Time:
    clock = pygame.time.Clock()
    FPS = 60 #frames per second / frame rate

    #Game Loop:
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        #Player Movement:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            player_1.move("up")
        if keys[pygame.K_s]:
            player_1.move("down")
        if keys[pygame.K_UP]:
            player_2.move("up")
        if keys[pygame.K_DOWN]:
            player_2.move("down")

        #Ball Movement and Collisions:
        ball.move()

        #Check for collisions with walls:
        if ball.y < 0 or ball.y > HEIGHT - ball.radius * 2:
            ball.bounce()
        if ball.x < 0 or ball.x > WIDTH - ball.radius * 2:
            ball.bounce()

        #Check for collisions with players:
        if ball.x < player_1.x + player_1.width and ball.x > player_1.x:
            if ball.y < player_1.y + player_1.height and ball.y > player_1.y:
                ball.bounce()
        if ball.x < player_2.x + player_2.width and ball.x > player_2.x:
            if ball.y < player_2.y + player_2.height and ball.y > player_2.y:
                ball.bounce()


        #Check for Scoring: (eventually)

        #Draw Game Objects:
        screen.fill((0,0,0))
        player_1.draw(screen)
        player_2.draw(screen)
        ball.draw(screen)
        pygame.display.flip()

        clock.tick(FPS)    

    pygame.quit()

if __name__ == '__main__':
    main()