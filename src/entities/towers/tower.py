import pygame
from src.entities.bullets.bullet import Bullet
from src.utils.gif_loader import load_gif_frames
class Tower:
    def __init__(self, x, y, width, height, health, shot_interval, background_image, damage, bullet_image=None):
        self.x = x
        self.y = y
        self.range_radius = 10
        self.width = width
        self.height = height
        self.health = health
        self.frames = load_gif_frames(background_image, self.width, self.height)
        self.current_frame = 0
        self.last_update = pygame.time.get_ticks()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.active = True
        self.bullet_image = bullet_image
        self.damage = damage
        self.last_shot_time = pygame.time.get_ticks()  # Armazena o momento do último tiro
        self.shot_interval = shot_interval  # Intervalo em milissegundos
        #self.background_image_opaque = background_image.fill((255, 255, 255, 128), special_flags=pygame.BLEND_RGBA_MULT) # Exemplo para 50% de opacidade

    def update(self):
        if self.health <= 0 :
            self.kill()
        now = pygame.time.get_ticks()
        if now - self.last_update > self.shot_interval/(len(self.frames)):
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
        
    def shoot(self):
        # Assumindo que a torre atira horizontalmente para a direita e aparece no centro da torre
        bullet_x = self.x + self.width // 2
        bullet_y = self.y + self.height // 2
        new_bullet = Bullet(bullet_x, bullet_y, size=20, speed=2, damage=self.damage, image=self.bullet_image, durability=1)
        return new_bullet
    
    
    def verify_to_shoot(self, enemies):
        for enemy in enemies:
            if enemy.y == self.y:
                return True
        return False
    

    def try_to_shoot(self, current_time, enemies):
        # Verifica se já passou o tempo suficiente desde o último tiro
        if current_time - self.last_shot_time > self.shot_interval and self.verify_to_shoot(enemies):
            self.last_shot_time = current_time
            return self.shoot()
        return None
    
    def draw(self, screen):
        screen.blit(self.frames[self.current_frame], (self.x, self.y))

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.kill()
    
    def kill(self):
        self.active = False


    
# class MoneyTower(Tower):
#     def __init__(self, x, y, width, height, health, shot_interval, background_image, damage, coin_image):
#         self.coin_image = coin_image

#         super().__init__(x, y, width, height, health, shot_interval, background_image, damage)

#     def try_to_shoot(self, current_time, enemies):
#         return super().try_to_shoot(current_time, enemies)

#     def update_money(self, current_time, player):
#         if current_time - self.last_shot_time > self.shot_interval:
#             player.hud.update_money(player.money)

#         super().update_money( current_time, player)
            
class MoneyTower(Tower):
    def __init__(self, x, y, width, height, health, shot_interval, background_image, damage, coin_image):
        super().__init__(x, y, width, height, health, shot_interval, background_image, damage)
        self.coin_image = coin_image
        self.last_money_time = pygame.time.get_ticks()  # Armazena o momento da última geração de dinheiro
        self.money_interval = 5000  # Intervalo em milissegundos para gerar dinheiro
        self.money_amount = 10  # Quantidade de dinheiro a ser gerada
        self.active = True  # A torre está sempre ativa, pois não atira nos inimigos

    def update(self):
        self.generate_money()  # Gera dinheiro ao longo do tempo

    def generate_money(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_money_time > self.money_interval:
            # Gera uma moeda na posição da torre
            self.last_money_time = current_time
            return True
        
    def draw(self, screen):
        screen.blit(self.frames[self.current_frame], (self.x, self.y))
