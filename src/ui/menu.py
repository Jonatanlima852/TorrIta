import pygame
import sys
from src.utils.button import Button
from src.utils.button import ButtonEscrito
from src.entities.player import Player
from src.entities.attack import Attack
from src.ui.grid import Grid
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT




class Menu:
    def __init__(self, screen):
        self.screen = screen
        pause_button_image = pygame.image.load('pause.png').convert_alpha()
        self.pause_button = Button(SCREEN_WIDTH - 80, 10, pause_button_image, 0.1, self.screen)
        self.game_paused = False


    def draw_text(self, center_x, center_y, text, font, screen, color=(255, 255, 255)):
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(center=(center_x, center_y))
        screen.blit(text_surf, text_rect)

    def main_menu(self):
        font = pygame.font.SysFont(None, 56)
        clock = pygame.time.Clock()
        running = True

        while running:
            self.screen.fill((0, 0, 0))  # Preenche a tela com preto

            self.draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, "TorrIta", font, self.screen)
            self.draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, "Press SPACE to Start", font, self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return  # Começa o jogo

            clock.tick(60)

    def pause_menu(self):
        font = pygame.font.SysFont(None, 56)
        clock = pygame.time.Clock()

        # Botão para sair
        botao_sair = ButtonEscrito(self.screen, "Sair", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150, font, (255, 255, 255), (100, 100, 255))
        # Botão para voltar ao menu inicial
        botao_voltar = ButtonEscrito(self.screen, "Voltar ao Menu Inicial", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, font, (255, 255, 255), (100, 100, 255))

        while self.game_paused:
            self.screen.fill((0, 0, 0))  # Preenche a tela com preto

            self.draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, "Paused", font, self.screen)
            self.draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, "Press SPACE to Resume", font, self.screen)

            # Desenha e verifica se os botões estão sob o mouse
            posicao_mouse = pygame.mouse.get_pos()
            botao_voltar.check_hover(posicao_mouse)
            botao_voltar.draw()
            botao_sair.check_hover(posicao_mouse)
            botao_sair.draw()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if botao_voltar.rect.collidepoint(event.pos):
                        self.game_paused = False
                        self.main_menu()  # Chama o menu principal diretamente
                        return
                    elif botao_sair.rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_paused = False  # Retoma o jogo
                        return

            clock.tick(60)


    def pause(self):
        self.game_paused = True

    