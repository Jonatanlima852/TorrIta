import pygame
import sys
from src.utils.button import Button
from src.utils.button import ButtonEscrito
from src.entities.player import Player
from src.entities.attack import Attack
from src.ui.grid import Grid
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, COR_FUNDO, COR_HOVER

class Menu:
    def __init__(self, screen):
        self.screen = screen
        pause_button_image = pygame.image.load('assets/images/pause.png').convert_alpha()
        self.pause_button = Button(SCREEN_WIDTH - 80, 10, pause_button_image, 0.1, self.screen)
        self.game_paused = False
        self.game_over = False
        self.win = False
        self.selected_difficulty = "normal"
        self.background_image = pygame.image.load('assets/images/background_menu.png').convert()
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


    def draw_text(self, center_x, center_y, text, font, screen, color=(255, 255, 255)):
        text_surf = font.render(text, True, color)
        text_rect = text_surf.get_rect(center=(center_x, center_y))
        screen.blit(text_surf, text_rect)

    def main_menu(self):
        fontnome = pygame.font.SysFont(None, 150)
        font = pygame.font.SysFont(None, 56)
        clock = pygame.time.Clock()
        running = True
        easy_button = ButtonEscrito(self.screen, "EASY", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40, font, COR_FUNDO, COR_HOVER)
        normal_button = ButtonEscrito(self.screen, "NORMAL", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 90, font, COR_FUNDO, COR_HOVER)
        hard_button = ButtonEscrito(self.screen, "HARD", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 140, font, COR_FUNDO, COR_HOVER)
        self.screen.blit(self.background_image, (0, 0))
        pygame.mixer.music.load('assets/music/menu_music.mp3')  # Substitua 'menu_music.mp3' pelo nome correto do arquivo de música
        pygame.mixer.music.set_volume(1)  # Ajuste o volume se necessário
        pygame.mixer.music.play(-1)

        easy_button.deselect()
        normal_button.deselect()
        hard_button.deselect()



        while running:

            #self.draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, "TorrIta", font, self.screen)
            #self.draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, "Press SPACE to Start", font, self.screen)

            # Desenha o título do jogo
            self.draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200, "TorrIta", fontnome, self.screen, (110, 100, 0))
        
        # Instrução para escolha da dificuldade
            self.draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, "Escolha a Dificuldade:", font, self.screen, COR_FUNDO)
        
        # Desenha instrução para iniciar o jogo
            self.draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200, "Pressione ESPAÇO para Iniciar", font, self.screen, COR_FUNDO)

            posicao_mouse = pygame.mouse.get_pos()
            for button in [easy_button, normal_button, hard_button]:
                button.check_hover(posicao_mouse)
                button.draw()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if easy_button.rect.collidepoint(event.pos):
                        easy_button.select()
                        normal_button.deselect()
                        hard_button.deselect()
                        self.selected_difficulty = "easy"
                    elif normal_button.rect.collidepoint(event.pos):
                        normal_button.select()
                        easy_button.deselect()
                        hard_button.deselect()
                        self.selected_difficulty = "normal"
                    elif hard_button.rect.collidepoint(event.pos):
                        hard_button.select()
                        easy_button.deselect()
                        normal_button.deselect()
                        self.selected_difficulty = "hard"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        return  


            clock.tick(60)


    def pause_menu(self):
        fontpause = pygame.font.SysFont(None, 90)
        font = pygame.font.SysFont(None, 56)
        clock = pygame.time.Clock()

        # Botão para sair
        botao_sair = ButtonEscrito(self.screen, "Sair", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80, font, COR_FUNDO, (100, 100, 255))
        # Botão para voltar ao menu inicial
        botao_voltar = ButtonEscrito(self.screen, "Voltar ao Menu Inicial", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 , font, COR_FUNDO, (100, 100, 255))

        while self.game_paused:
            self.screen.blit(self.background_image, (0, 0))

            self.draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200, "Paused", fontpause, self.screen, COR_FUNDO)
            self.draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 200, "Press SPACE to Resume", font, self.screen, COR_FUNDO)

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
                        #self.main_menu()  # Chama o menu principal diretamente
                        return "restart"
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


    def gameover_menu(self):
        fontpause = pygame.font.SysFont(None, 90)
        font = pygame.font.SysFont(None, 56)
        clock = pygame.time.Clock()

        # Botão para sair
        botao_sair = ButtonEscrito(self.screen, "Sair", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80, font, (255,255,255), (100, 100, 255))
        # Botão para voltar ao menu inicial
        botao_voltar = ButtonEscrito(self.screen, "Voltar ao Menu Inicial", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, font, (255,255,255), (100, 100, 255))

        running = True
        while running:
            self.screen.fill((0, 0, 0))  # Preenche a tela com preto

            # Desenha o texto de game over
            self.draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200, "SE DEU MAL!", fontpause, self.screen, (255, 0, 0))  # Texto vermelho

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
                        return "restart"  # Indica que o usuário quer reiniciar o jogo
                    elif botao_sair.rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                        return

            clock.tick(60)

    def win_menu(self):
        fontpause = pygame.font.SysFont(None, 90)
        font = pygame.font.SysFont(None, 56)
        clock = pygame.time.Clock()

        # Botão para sair
        botao_sair = ButtonEscrito(self.screen, "Sair", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80, font, (255,255,255), (100, 100, 255))
        # Botão para voltar ao menu inicial
        botao_voltar = ButtonEscrito(self.screen, "Voltar ao Menu Inicial", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, font, (255,255,255), (100, 100, 255))

        running = True
        while running:
            self.screen.fill((0, 0, 0))  # Preenche a tela com preto

            # Desenha o texto de game over
            self.draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 200, "VENCEU!", fontpause, self.screen, (0, 255, 0))  # Texto vermelho

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
                        return "restart"  # Indica que o usuário quer reiniciar o jogo
                    elif botao_sair.rect.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
                        return

            clock.tick(60)
    