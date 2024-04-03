import pygame


class Button:
    def __init__(self, x, y, image, scale, screen):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.screen = screen

    def draw(self):
        # Desenhe o botão na tela
        self.screen.blit(self.image, (self.rect.x, self.rect.y))

    def verify_click(self):
        # Verifique a posição do mouse e as condições de clique
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

class ButtonEscrito:
    def __init__(self, screen, text, x, y, font, color_normal, color_hover, center=True):
        self.screen = screen
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.color_normal = color_normal
        self.color_hover = color_hover
        self.center = center
        self.color = self.color_normal
        self.render_text()

    def render_text(self):
        self.text_rendered = self.font.render(self.text, True, self.color)
        self.rect = self.text_rendered.get_rect()
        if self.center:
            self.rect.center = (self.x, self.y)
        else:
            self.rect.topleft = (self.x, self.y)

    def draw(self):
        self.screen.blit(self.text_rendered, self.rect)

    def check_hover(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.color = self.color_hover
        else:
            self.color = self.color_normal
        self.render_text()
        