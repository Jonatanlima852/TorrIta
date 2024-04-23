import pygame
from src.entities.player import Player
from src.entities.attack import Attack
from src.ui.grid import Grid
from src.ui.hud import HUD  # Garanta que esteja importando corretamente baseado na sua estrutura de diretório
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Game:
    def __init__(self, screen, dificuldade):
        self.screen = screen
        self.attack  = Attack(dificuldade)
        self.grid = Grid(SCREEN_HEIGHT/6, SCREEN_WIDTH/11, 5, 9)
        self.hud = HUD(screen, 1000)  # Inicializa o HUD
        self.player = Player(self.grid, self.hud, SCREEN_WIDTH/11, SCREEN_HEIGHT/6,)
        self.dificuldade = dificuldade


    

    def update(self):
        self.attack.update(self.player.towers)
        self.player.update(self.attack.enemies)
    
    def draw(self):
        # self.grid.desenhar_retangulo(self.screen)
        # self.grid.desenhar_linhas(self.screen)
        self.grid.desenhar_fundo(self.screen)
        self.player.draw(self.screen)
        self.attack.draw(self.screen)
        self.hud.draw()  # Desenha o HUD por cima de tudo

