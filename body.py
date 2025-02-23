import pygame as pg

class Body:
    def __init__(self, x, y, mass, radius,
                 velocity_x = 0, velocity_y = 0, 
                 acceleration_x = 0, acceleration_y = 0,
                 color=(255,255,255)):
        self.mass = mass
        self.radius = radius
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.acceleration_x = acceleration_x
        self.acceleration_y = acceleration_y
        self.color = color

    def draw(self, screen):
        pg.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius) # draws the body onto the screen
