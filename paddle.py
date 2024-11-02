import pygame

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