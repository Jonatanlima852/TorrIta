import pygame
from src.entities.bullets.bullet import Bullet
from src.utils.gif_loader import load_gif_frames
class Tower:
    def __init__(self, x, y, width, height, health, background_image):
        self.x = x
        self.y = y
        self.range_radius = 10
        self.width = width
        self.height = height
        self.health = health
        self.frames = load_gif_frames(background_image, self.width, self.height)
        self.current_frame = 0
        self.animation_speed = 0.1  # Ajuste isso conforme a velocidade desejada da animação
        self.last_update = pygame.time.get_ticks()

        self.last_shot_time = pygame.time.get_ticks()  # Armazena o momento do último tiro
        self.shot_interval = 2000  # Intervalo em milissegundos
        #self.background_image_opaque = background_image.fill((255, 255, 255, 128), special_flags=pygame.BLEND_RGBA_MULT) # Exemplo para 50% de opacidade

    def update(self):
        if self.health <= 0 :
            self.kill()
        now = pygame.time.get_ticks()
        if now - self.last_update > 1000 * self.animation_speed:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
        
    def shoot(self):
        # Assumindo que a torre atira horizontalmente para a direita e aparece no centro da torre
        bullet_x = self.x + self.width // 2
        bullet_y = self.y + self.height // 2
        new_bullet = Bullet(bullet_x, bullet_y, size=20, speed=2, damage=10, durability=1)
        return new_bullet
    
    def try_to_shoot(self, current_time):
        # Verifica se já passou o tempo suficiente desde o último tiro
        if current_time - self.last_shot_time > self.shot_interval:
            self.last_shot_time = current_time
            return self.shoot()
        return None
    
    def draw(self, screen):
        screen.blit(self.frames[self.current_frame], (self.x, self.y))