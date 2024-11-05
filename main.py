import pygame
from paddle import Paddle
from ball import Ball
from config import *

def main():
    pygame.init()

    #Display:
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
    pygame.display.set_caption('Pong Game')

    #Game Objects:
    player_1 = Paddle(10,100,10,100,'red')
    player_2 = Paddle(WIDTH - 20,100,10,100,'blue')
    ball = Ball(10,'white')

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
        wall_collision(ball, HEIGHT, WIDTH)

        #Check for collisions with players:
        player_collision(ball, player_1, player_2)


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