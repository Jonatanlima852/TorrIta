import pygame

class Tower:
    def __init__(self, x, y, width, height, health):
        self.x = x
        self.y = y
        self.range_radius = 10
        self.width = width
        self.height = height
        self.health = health

    def update(self):
        if self.health <= 0 :
            self.kill()