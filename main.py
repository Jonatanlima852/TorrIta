# main.py
import pygame
from src.game import Game
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.ui.menu import Menu


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("TorrIta")
    
    menu = Menu(screen)
    menu.main_menu()  # Exibe o menu principal antes de iniciar o jogo

    clock = pygame.time.Clock()
    game = Game(screen)

    running = True
    # game_paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if menu.game_paused:
            menu.pause_menu()

        else:
            # Atualizações do jogo
            game.update()

            # Desenho na Tela 
            screen.fill((0, 0, 0))  # Preenche a tela com preto
            game.draw()

            menu.pause_button.draw()
            menu.pause_button.verify_click()
            if(menu.pause_button.clicked):
                menu.pause()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()