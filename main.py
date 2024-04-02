# main.py
import pygame
from src.game import Game
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS



class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False
        # Verifique a posição do mouse e as condições de clique
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Desenhe o botão na tela
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

def draw_text(center_x, center_y, text, font, screen, color=(255, 255, 255)):
    text_surf = font.render(text, True, color)
    text_rect = text_surf.get_rect(center=(center_x, center_y))
    screen.blit(text_surf, text_rect)

def main_menu(screen):
    font = pygame.font.SysFont(None, 56)
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill((0, 0, 0))  # Preenche a tela com preto

        draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, "TorrIta", font, screen)
        draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, "Press SPACE to Start", font, screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return  # Começa o jogo

        clock.tick(60)

def pause_menu(screen, game_paused):
    font = pygame.font.SysFont(None, 56)
    clock = pygame.time.Clock()

    while game_paused:
        screen.fill((0, 0, 0))  # Preenche a tela com preto

        draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, "Paused", font, screen)
        draw_text(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, "Press SPACE to Resume", font, screen)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return  # Retorna ao jogo

        clock.tick(60)
    pause_button_image = pygame.image.load('pouse.png').convert_alpha()

    pause_button = Button(SCREEN_WIDTH - 70, 10, pause_button_image, 0.5)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TorrIta")
    
    main_menu(screen)  # Exibe o menu principal antes de iniciar o jogo

    # Instancia o botão de pausa aqui para que possa ser acessado no loop principal
    pause_button_image = pygame.image.load('pouse.png').convert_alpha()
    pause_button = Button(SCREEN_WIDTH - 70, 10, pause_button_image, 0.5)

    clock = pygame.time.Clock()
    game = Game(screen)

    running = True
    game_paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if game_paused:
            pause_menu(screen, game_paused)
            game_paused = False
        else:
            # Atualizações do jogo
            game.update()

            # Desenho na Tela 
            screen.fill((0, 0, 0))  # Preenche a tela com preto
            game.draw()

            # Verifica se o botão de pausa foi clicado
            if pause_button.draw(screen):  
                game_paused = not game_paused

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()