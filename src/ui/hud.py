import pygame
from src.entities.player import Player

class HUD:
    def __init__(self, screen, money, heart):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24)
        self.defense_buttons = []
        self.money = money
        self.life = heart
        self.init_defense_buttons()
        self.pause_button = None
        coin_image = pygame.image.load('assets/images/coin.png').convert_alpha()
        hud_image = pygame.image.load('assets/images/hud.png').convert_alpha()
        heart_image = pygame.image.load('assets/images/coracao.png').convert_alpha()
        self.coin_image = pygame.transform.scale(coin_image, (32, 32))
        self.heart_image = pygame.transform.scale(heart_image, (25, 25))
        self.defense_images = [pygame.image.load('assets/images/defesa_rui.jpg').convert_alpha(),
                               pygame.image.load('assets/images/defesa_petismo.jpg').convert_alpha(),
                               pygame.image.load('assets/images/defesa_bibs.jpg').convert_alpha(),
                               pygame.image.load('assets/images/Red_Bull.png').convert_alpha(),]
        self.selected_defense_index = 0  # Índice da defesa selecionada (exemplo)
        hud_height = 200
        hud_width = 500
        selection_indicator = pygame.image.load('assets/images/focus.png').convert_alpha()
        self.selection_indicator = pygame.transform.scale(selection_indicator, (70, 70))
        hud_image = pygame.image.load('assets/images/hud.png').convert_alpha()
        self.hud_image = pygame.transform.scale(hud_image, (hud_width, hud_height))



    def init_defense_buttons(self):
        button_width = 60
        button_height = 60
        button_margin = 20
        start_x = 120
        for i in range(4):
            x = start_x + i * (button_width + button_margin)
            y = 20
            button = pygame.Rect(x, y, button_width, button_height)
            self.defense_buttons.append(button)
        self.bg_end_x = self.defense_buttons[-1].right + 30


    def draw(self):
        self.screen.blit(self.hud_image, (-20, -50))

        coin_x = 20
        coin_y = 20
        self.screen.blit(self.coin_image, (coin_x, coin_y))
        self.screen.blit(self.heart_image, (coin_x + 3, coin_y + 30))

        money_display_x = coin_x + self.coin_image.get_width() + 5
        money_display = self.font.render(f"{self.money}", True, (255, 255, 0))
        self.screen.blit(money_display, (money_display_x, coin_y))
        heart_display_x = coin_x + self.heart_image.get_width() + 15
        heart_display = self.font.render(f"{self.life}", True, (255, 255, 255))
        self.screen.blit(heart_display, (heart_display_x, coin_y + 30))

        for button, defense_image in zip(self.defense_buttons, self.defense_images):
            button_width = 60
            button_height = 60
            pygame.draw.rect(self.screen, (255, 255, 255), button)
            button_center = button.center
            defense_image = pygame.transform.scale(defense_image, (button_width, button_height))
            image_rect = defense_image.get_rect(center=button_center)
            self.screen.blit(defense_image, image_rect.topleft)

        self.update()  # Índice da defesa selecionada (exemplo)
        selected_button = self.defense_buttons[self.selected_defense_index]

        # Desenha a imagem de indicação de seleção sobre o botão selecionado
        button_center = selected_button.center
        indicator_rect = self.selection_indicator.get_rect(center=button_center)
        self.screen.blit(self.selection_indicator, indicator_rect.topleft)

        if self.pause_button:
            self.pause_button.draw()

    def update_money(self, new_money):
        self.money = new_money

    
    def update_life(self, new_life):
        self.life = new_life

    # seleciona a torre para usar no player
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, button in enumerate(self.defense_buttons):
                    if button.collidepoint(mouse_pos):
                        self.selected_defense_index = i
                        