import pygame
import sys
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy:
    def __init__(self, x, y, size, health, damage):
        self.x = x
        self.y = y
        self.size = size
        self.color = pygame.Color('blue')
        self.speed = 5
        self.health = health #PRECISA DISSO
        self.damage = damage

    def update(self):
        self.x -= self.speed  # Move o inimigo horizontalmente
        if self.health <= 0 :
            self.kill()
