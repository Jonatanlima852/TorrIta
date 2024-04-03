import pygame
import sys

# Inicialização do Pygame
pygame.init()

# Definindo as dimensões da janela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo de Colisão")

# Definindo cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Definindo as classes para o jogador, bala e inimigo
class Player(pygame.sprite.Sprite):
    def _init_(self):
        super()._init_()
        self.image = pygame.Surface((50, 50))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

class Bullet(pygame.sprite.Sprite):
    def _init_(self, x, y):
        super()._init_()
        self.image = pygame.Surface((5, 10))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 7

    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def _init_(self, x, y):
        super()._init_()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

# Criando grupos de sprites
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Criando o jogador
player = Player()
all_sprites.add(player)

# Definindo a função principal do jogo
def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        # Limitando a taxa de quadros por segundo
        clock.tick(60)

        # Processando eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)

        # Atualizando sprites
        all_sprites.update()

        # Verificando colisões entre balas e inimigos
        hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
        for bullet, enemy in hits.items():
            # Ação a ser executada após a colisão (por exemplo, aumentar a pontuação)
            print("Bala atingiu um inimigo!")

        # Desenhando na tela
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        # Atualizando a tela
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "_main_":
    main()
