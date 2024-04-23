import pygame
import random
from src.entities.enemies.enemy import Enemy
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Attack:
    def __init__(self, dificuldade):
        self.enemies = []
        self.time_of_last_enemy = 0
        self.interval = 8000
        self.dificuldade = dificuldade


    def update(self, towers):
        self.update_enemies(towers)


    def draw(self, screen):
        for enemy in self.enemies:
            # Desenha a imagem do zumbi na tela ao invés de um retângulo vermelho
            screen.blit(enemy.image, (enemy.x, enemy.y))

    def update_enemies(self, towers):
        for enemy in self.enemies:
            enemy.update(towers)

        actual_time = pygame.time.get_ticks()
        if actual_time - self.time_of_last_enemy >= self.interval:
            # Atualize o tempo anterior para o momento atual e cria um novo inimigo
            self.time_of_last_enemy = actual_time
            value = int((random.randint(1, 5) * (SCREEN_HEIGHT / 6)))
            rand = int(random.randint(1,4))
            if self.dificuldade == "easy":
                fator = 1
            elif self.dificuldade == "normal":
                fator = 1.2
            elif self.dificuldade == "hard":
                fator = 1.4

            if rand != 2:
                new_enemy = Enemy(SCREEN_WIDTH, value, 20, fator*50, fator*20, 0.2)
            else:
                new_enemy = Enemy(SCREEN_WIDTH, value, 20, fator*80, fator*20, 0.2)
            self.enemies.append(new_enemy)
        
        self.enemies = [enemy for enemy in self.enemies if enemy.active]

