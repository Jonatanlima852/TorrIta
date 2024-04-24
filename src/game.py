import pygame
from src.entities.player import Player
from src.entities.attack import Attack
from src.ui.grid import Grid
from src.ui.hud import HUD 
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Game:
    def __init__(self, screen, dificuldade):
        self.screen = screen
        self.attack  = Attack(dificuldade)
        self.grid = Grid(SCREEN_HEIGHT/6, SCREEN_WIDTH/11, 5, 9)
        self.hud = HUD(screen, 1000, 5)
        self.player = Player(self.grid, self.hud, SCREEN_WIDTH/11, SCREEN_HEIGHT/6, self)
        self.dificuldade = dificuldade


    

    def update(self):
        self.attack.update(self.player.towers)
        self.player.update(self.attack.enemies)
    
    def draw(self):
        self.grid.desenhar_fundo(self.screen)
        self.player.draw(self.screen)
        self.attack.draw(self.screen)
        self.hud.draw()

    def game_over_screen(self):
        font = pygame.font.Font(None, 74)
        text = font.render('SE FUDEU!', True, (255, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

        while True:
            self.screen.fill((0, 0, 0))  # Limpar tela
            self.screen.blit(text, text_rect)  # Mostrar texto
            pygame.display.flip()  # Atualizar tela

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return  # Pode alterar para reiniciar o jogo