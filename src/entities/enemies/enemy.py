import pygame
import sys
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy:
    def __init__(self, x, y, size, health, damage):
        self.x = x
        self.y = y
        self.size = size
        self.speed = 0.2
        self.health = health 
        self.damage = damage
        zombie_walk1 = pygame.image.load("assets/images/zombie/zombie_walk1.png").convert_alpha()
        zombie_walk2 = pygame.image.load("assets/images/zombie/zombie_walk2.png").convert_alpha()
        zombie_walk3 = pygame.image.load("assets/images/zombie/zombie_walk3.png").convert_alpha()
        self.zombie_walk = [zombie_walk1, zombie_walk2, zombie_walk3, zombie_walk2]
        self.image = self.zombie_walk[0]
        self.animation_index = 0
        self.animation_speed = 20  # Aumente este valor para diminuir a velocidade da animação
        self.animation_counter = 0
        self.rect = pygame.Rect(self.x,self.y,size,size)

    def update(self):
        self.animation_state()
        self.x -= self.speed  # Move o inimigo horizontalmente
        self.rect.x = self.x
        

    def animation_state(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.image = self.zombie_walk[self.animation_index]
            self.animation_index += 1
            if self.animation_index >= len(self.zombie_walk):
                self.animation_index = 0
            self.animation_counter = 0  # Reset the counter after updating the frame

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()

    def kill(self):
        global enemies  # Se os zumbis estão gerenciados globalmente
        enemies.remove(self)