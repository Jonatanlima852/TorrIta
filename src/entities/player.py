import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from src.entities.towers.tower import Tower
from src.ui.grid import Grid
class Player:
    def __init__(self, x, y, width_of_grid, height_of_grid):
        self.x = x
        self.y = y
        self.size = 10
        self.color = (255, 0, 0)  # Vermelho
        self.color_weak = (100, 0, 0)  # Vermelho fraco
        self.speed = 5
        self.towers = []
        self.grid = Grid(SCREEN_HEIGHT/6, SCREEN_WIDTH/11, 5, 9)  # Verificar se é possível melhorar a lógica disso
        self.width_of_grid = width_of_grid
        self.height_of_grid = height_of_grid



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
        # Desenha prévia da Torre
        x, y = pygame.mouse.get_pos()
        w = self.width_of_grid
        h = self.height_of_grid
        allowed, x_ret, y_ret = self.grid.retify_to_grid(x, y)
        if allowed:
            pygame.draw.rect(screen, self.color, (x_ret, y_ret, w, h))

        # Desenha todas as torres do jogo
        for tower in self.towers:
            pygame.draw.rect(screen, self.color_weak, (tower.x, tower.y, tower.width, tower.height))


    def update_towers(self):
        # self.last_mouse_click  = pygame.mouse.get_pressed()
        if pygame.mouse.get_pressed()[0]:  # Botão esquerdo do mouse
            x, y = pygame.mouse.get_pos()
            allowed, x_ret, y_ret = self.grid.retify_to_grid(x, y)
            if allowed:
                new_tower = Tower(x_ret, y_ret, self.width_of_grid, self.height_of_grid, 20)
                self.towers.append(new_tower)


    def update_coins(self):
        pass


    def update_life(self):
        pass