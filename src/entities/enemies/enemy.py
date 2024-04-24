import pygame
import sys
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Enemy:
    def __init__(self, x, y, size, health, damage, speed, images):
        self.x = x - 2*SCREEN_WIDTH/11
        self.y = y
        self.size = size
        self.speed = speed
        self.health = health 
        self.damage = damage
        self.zombie_walk = images
        self.image = self.zombie_walk[0]
        self.animation_index = 0
        self.animation_speed = 40  # Aumente este valor para diminuir a velocidade da animação
        self.animation_counter = 0
        self.rect = pygame.Rect(self.x, self.y+50, size, size)
        self.active = True
        self.is_attacking = False
        self.target = None
        self.last_attack_time = 0
        self.interval_damage = 1000
        

    def update(self, towers):
        if not self.is_attacking:
            self.x -= self.speed  # Move o inimigo horizontalmente
            self.rect.x = self.x

        if not self.active:
            return
        self.animation_state()

        if self.is_attacking and self.target:
            self.give_damage(self.target)

        for tower in towers:
            if self.rect.colliderect(tower.rect):
                self.is_attacking = True
                self.target = tower
                break
        

    def animation_state(self):
        self.animation_counter += 1
        if self.animation_counter >= self.animation_speed:
            self.image = self.zombie_walk[self.animation_index]
            self.animation_index += 1
            if self.animation_index >= len(self.zombie_walk):
                self.animation_index = 0
            self.animation_counter = 0  # Reset the counter after updating the frame

    def give_damage(self, tower):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_attack_time >= self.interval_damage:  # ataca a cada segundo
            self.last_attack_time = current_time
            tower.take_damage(self.damage)
            if tower.health <= 0:
                self.is_attacking = False
                self.target = None
    
    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()

    def kill(self):
        self.active = False

def load_images(paths):
    images = []
    for path in paths:
        image = pygame.image.load(path).convert_alpha()
        image = pygame.transform.scale(image, (SCREEN_WIDTH/11, SCREEN_HEIGHT/6))
        images.append(image)
    return images

class WeakEnemy(Enemy):
    def __init__(self, x, y, size, health, damage, speed):
        images = load_images([
            "assets/bolacha/1.png",
            "assets/bolacha/2.png",
            "assets/bolacha/3.png",
            "assets/bolacha/2.png",
        ])
        super().__init__(x, y, size, health, damage, speed, images)

class StrongEnemy(Enemy):
    def __init__(self, x, y, size, health, damage, speed):
        images = load_images([
            "assets/goiano/1.png",
            "assets/goiano/2.png",
            "assets/goiano/3.png",
            "assets/goiano/2.png",
        ])
        super().__init__(x, y, size, health, damage, speed, images)