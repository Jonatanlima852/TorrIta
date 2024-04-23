import pygame

class HUD:
    def __init__(self, screen, money):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 24)
        self.defense_buttons = []
        self.money = money
        self.init_defense_buttons()
        self.pause_button = None
        coin_image = pygame.image.load('assets/images/coin.png').convert_alpha()
        self.coin_image = pygame.transform.scale(coin_image, (32, 32))
        self.bg_color = (139, 69, 19)

    def init_defense_buttons(self):
        button_width = 60
        button_height = 60
        button_margin = 20
        start_x = 120
        for i in range(4):
            x = start_x + i * (button_width + button_margin)
            y = 10
            button = pygame.Rect(x, y, button_width, button_height)
            self.defense_buttons.append(button)
        self.bg_end_x = self.defense_buttons[-1].right + 30

    def draw(self):
        hud_height = self.coin_image.get_height() + 68
        pygame.draw.rect(self.screen, self.bg_color, (0, 0, self.bg_end_x, hud_height))

        coin_x = 10
        coin_y = 20
        self.screen.blit(self.coin_image, (coin_x, coin_y))

        money_display_x = coin_x + self.coin_image.get_width() + 10
        money_display = self.font.render(f"${self.money}", True, (255, 255, 255))
        self.screen.blit(money_display, (money_display_x, coin_y))

        for button in self.defense_buttons:
            pygame.draw.rect(self.screen, (255, 255, 255), button)

        if self.pause_button:
            self.pause_button.draw()

    def update_money(self, new_money):
        self.money = new_money

