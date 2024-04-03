import pygame

class Bullet:
    def __init__(self, x, y, size, speed, damage, durability):
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.damage = damage
        self.durability = durability

    def update(self):
        self.x += self.speed  # Move a bala horizontalmente
        if self.durability <= 0 :
            self.kill()    

    

