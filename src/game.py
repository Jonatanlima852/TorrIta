import pygame
from src.entities.player import Player
from src.entities.attack import Attack
from src.ui.grid import Grid
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.attack  = Attack()
        self.grid = Grid()

    def update(self):
        self.player.update()
        self.attack.update()

    def draw(self):
        self.grid.desenhar_retangulo(self.screen)
        self.grid.desenhar_linhas(self.screen)
        self.player.draw(self.screen)
        self.attack.draw(self.screen)
