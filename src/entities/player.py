import pygame
from src.entities.towers.tower import Tower

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 10
        self.color = (255, 0, 0)  # Vermelho
        self.speed = 5
        self.towers = []


    def update(self):
        self.update_towers()
        self.update_coins()
        self.update_life()
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
        for tower in self.towers:
            pygame.draw.rect(screen, self.color, (tower.x, tower.y, tower.size, tower.size))


    def update_towers(self):
        # self.last_mouse_click  = pygame.mouse.get_pressed()
        if pygame.mouse.get_pressed()[0]:  # Botão esquerdo do mouse
            x, y = pygame.mouse.get_pos()
            new_tower = Tower(x, y, 10)
            self.towers.append(new_tower)


    def update_coins(self):
        pass


    def update_life(self):
        pass