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
        hud_image = pygame.image.load('assets/images/hud.png').convert_alpha()
        self.coin_image = pygame.transform.scale(coin_image, (32, 32))
        hud_height = 200
        hud_width = 500
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
        coin_y = 30
        self.screen.blit(self.coin_image, (coin_x, coin_y))

        money_display_x = coin_x + self.coin_image.get_width() + 5
        money_display = self.font.render(f"{self.money}", True, (255, 255, 0))
        self.screen.blit(money_display, (money_display_x, coin_y))

        for button in self.defense_buttons:
            pygame.draw.rect(self.screen, (255, 255, 255), button)

        if self.pause_button:
            self.pause_button.draw()

    def update_money(self, new_money):
        self.money = new_money