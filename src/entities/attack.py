import pygame
import random
from src.entities.enemies.enemy import Enemy
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Attack:
    def __init__(self):
        # self.x = x
        # self.y = y
        # self.size = 10
        # self.color = (255, 0, 0)  # Vermelho
        # self.speed = 5
        self.enemies = []
        self.time_of_last_enemy = 0
        self.interval = 8000


    def update(self):
        self.update_enemies()
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_LEFT]:
    #         self.x -= self.speed
    #     if keys[pygame.K_RIGHT]:
    #         self.x += self.speed
    #     if keys[pygame.K_UP]:
    #         self.y -= self.speed
    #     if keys[pygame.K_DOWN]:
    #         self.y += self.speed


    def draw(self, screen):
        for enemy in self.enemies:
            # Desenha a imagem do zumbi na tela ao invés de um retângulo vermelho
            screen.blit(enemy.image, (enemy.x, enemy.y))

    def update_enemies(self):
        for enemy in self.enemies:
            enemy.update()

        actual_time = pygame.time.get_ticks()
        if actual_time - self.time_of_last_enemy >= self.interval:
            # Atualize o tempo anterior para o momento atual e cria um novo inimigo
            self.time_of_last_enemy = actual_time
            value = int((random.randint(1, 5) * (SCREEN_HEIGHT / 6)))
            new_enemy = Enemy(SCREEN_WIDTH, value, 20, 80, 20)
            self.enemies.append(new_enemy)
        
        self.enemies = [enemy for enemy in self.enemies if enemy.active]

