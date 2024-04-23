import pygame
from src.settings import SCREEN_WIDTH

class Bullet:
    def __init__(self, x, y, size, speed, damage, durability):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.damage = damage
        self.durability = durability
        self.active = True
        self.image = pygame.image.load("assets/images/tiro.png")
        self.rect = pygame.Rect(self.x, self.y, size, size)

    def update(self, enemies):
        if not self.active:
            return  # Se a bala não está ativa, não faz nada

        self.x += self.speed
        self.rect.x = self.x
        if self.x > SCREEN_WIDTH or self.durability <= 0:
            self.kill()
        else:
            self.check_collision(enemies)

    def check_collision(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.take_damage(self.damage)
                self.kill()
                break

    def kill(self):
        self.active = False  # Marca a bala como inativ


    

