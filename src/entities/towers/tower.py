import pygame

class Tower:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.range_radius = 10
        self.width = width
        self.height = height