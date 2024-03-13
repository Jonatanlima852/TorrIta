import pygame
from src.entities.player import Player
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # def update(self):
    #     self.player.update()

    def draw(self):
        self.screen.fill((0, 0, 0))  # Preenche a tela com preto
        self.player.draw(self.screen)

    def put_tower(self):
        self.player.put_tower(self.screen)