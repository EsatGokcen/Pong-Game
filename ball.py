import pygame
import random

class Ball:
    
    def __init__(self,x,y,radius,color):
        self.x = 400
        self.y = 300
        self.radius = radius
        self.color = color
        self.x_vel = random.randint(-15,15)
        self.y_vel = random.randint(-15,15)
        if self.x_vel == 0 and self.y_vel == 0: #makes sure ball is always moving
            self.x_vel = random.randint(-15,15)
            self.y_vel = random.randint(-15,15)

    def draw(self,screen):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)
    
    def move(self):
        self.x = self.x + self.x_vel
        self.y = self.y + self.y_vel


    def bounce(self):
        self.x_vel *= -1 #multiplying x coords with -1 will reverse their direction
        self.y_vel = random.randint(-5,5)