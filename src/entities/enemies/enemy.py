import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy:
    def __init__(self, size):
        self.x = SCREEN_WIDTH
        self.y = SCREEN_HEIGHT/2
        self.size = size
        self.color = pygame.Color('blue')
        self.speed = 2

    def update(self):
        self.x -= self.speed  # Move o inimigo horizontalmente
