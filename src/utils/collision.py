import pygame
import sys
from src.entities.bullets import bullet
from src.entities.enemies import enemy
from src.entities.towers import tower

hits1 = pygame.sprite.groupcollide(bullet, enemy, True, True)
for bullet, enemy in hits1.items():
    bullet.durability = bullet.durability - 1
    enemy.health = enemy.health - bullet.damage
    #ganhar moeda

hits2 = pygame.sprite.groupcollide(tower, enemy, True, True)
for tower, enemy in hits1.items():
    tower.health = tower.health - enemy.damage
    #enemy.speed = 0 