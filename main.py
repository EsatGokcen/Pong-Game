import pygame

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