import pygame

class Tower:
    def __init__(self, x, y, width, height, health, background_image):
        self.x = x
        self.y = y
        self.range_radius = 10
        self.width = width
        self.height = height
        self.health = health
        self.background_image = background_image
        #self.background_image_opaque = background_image.fill((255, 255, 255, 128), special_flags=pygame.BLEND_RGBA_MULT) # Exemplo para 50% de opacidade

    def update(self):
        if self.health <= 0 :
            self.kill()