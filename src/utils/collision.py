import pygame
import sys
from src.entities.bullets import Bullet
from src.entities.enemies import Enemy

hits = pygame.sprite.groupcollide(bullet, enemy, True, True)
for bullet, enemy in hits.items():
    bullet.durability = bullet.durability - 1
    enemy.health = enemy.health - bullet.damage
    #ganhar moeda

