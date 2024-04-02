import pygame
from src.utils.button import Button
from src.entities.player import Player
from src.entities.attack import Attack
from src.ui.grid import Grid
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT




class Menu:
    def __init__(self, screen):
        self.screen = screen
        pause_button_image = pygame.image.load('pouse.png').convert_alpha()
        self.pause_button = Button(SCREEN_WIDTH - 70, 10, pause_button_image, 0.5, self.screen)
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

        while self.game_paused:
            self.screen.fill((0, 0, 0))  # Preenche a tela com preto

            self.draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, "Paused", font, self.screen)
            self.draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, "Press SPACE to Resume", font, self.screen)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.game_paused = False
                        return  # Retorna ao jogo

            clock.tick(60)


    def pause(self):
        self.game_paused = True

    