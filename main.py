# main.py
import pygame
from src.game import Game
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from src.ui.menu import Menu
from src.ui.hud import HUD


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.mouse.set_cursor(*pygame.cursors.tri_left)
    pygame.display.set_caption("TorrIta")
    
    menu = Menu(screen)
    menu.main_menu()

    clock = pygame.time.Clock()
    game = Game(screen, menu.selected_difficulty, menu)
    start_time = pygame.time.get_ticks()

    running = True

    while running:
        current_time = pygame.time.get_ticks()
        if current_time - start_time >= 120000:
            reiniciar = menu.win_menu()
            if reiniciar == "restart":
                main()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if menu.game_paused:
            reiniciar = menu.pause_menu() 
            if reiniciar == "restart":
                main()
        if menu.game_over:
            reiniciar = menu.gameover_menu() 
            if reiniciar == "restart":
                main()
        


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