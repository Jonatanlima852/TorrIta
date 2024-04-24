import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT
from src.entities.towers.tower import Tower
from src.ui.grid import Grid

DEBOUNCE_INTERVAL = 500
class Player:
    def __init__(self, grid, hud, width_of_grid, height_of_grid, menu):
        self.towers = []
        self.bullets = []
        self.grid = grid  # Verificar se é possível melhorar a lógica disso
        self.hud = hud  # Verificar se é possível melhorar a lógica disso
        self.money = self.hud.money # Dinheiro inicial, pode ser modificado ou ajustado conforme a dificuldade
        self.width_of_grid = width_of_grid
        self.height_of_grid = height_of_grid
        self.image_tower_opaque = pygame.image.load("assets/images/Red_Bull.png").convert_alpha() #.fill((255, 255, 255, 128), special_flags=pygame.BLEND_RGBA_MULT) # Exemplo para 50% de opacidade
        self.image_tower_opaque = pygame.transform.scale(self.image_tower_opaque, (self.width_of_grid, self.height_of_grid))
        #self.image_tower_opaque = self.image_tower_opaque.fill((255, 255, 255, 128), special_flags=pygame.BLEND_RGBA_MULT)

        # Crie uma superfície transparente com o mesmo tamanho da sua imagem
        self.surface_transparent = pygame.Surface((self.width_of_grid, self.height_of_grid)).convert_alpha()

        # Defina a opacidade da superfície (0 a 255)
        self.surface_transparent.set_alpha(128)  # 50% de opacidade

        # Desenhe sua imagem na superfície transparente
        # self.surface_transparent.blit(self.image_tower_opaque, (0, 0))  # Desenhe no canto superior esquerdo da superfície transparente
        self.last_click_time = 0
        # self.game = game
        self.life = 5
        self.menu = menu

        # possíveis defesas da classe
        self.defenses = [
            {
                "index": 0,
                "price": 100,
                "shot_interval": 2000,
                "health": 60,
                "damage": 10,
                "bullet_image": pygame.image.load("assets/images/tiro.png").convert_alpha(),
                "img_estatica": pygame.transform.scale(pygame.image.load("assets/images/defesa_rui.jpg").convert_alpha(), (self.width_of_grid, self.height_of_grid)),
                "gif": "assets/gifs/rui_atirando.gif",
            },
            {
                "index": 1,
                "price": 100,
                "shot_interval": 10000000,
                "health": 200,
                "damage": 0,
                "bullet_image": pygame.image.load("assets/images/tiro.png").convert_alpha(),
                "img_estatica": pygame.transform.scale(pygame.image.load("assets/images/defesa_petismo.jpg").convert_alpha(), (self.width_of_grid, self.height_of_grid)),
                "gif": "assets/gifs/petismo_atirando.png",
            },
            {
                "index": 2,
                "price": 100,
                "shot_interval": 3000,
                "health": 21,
                "damage": 20,
                "bullet_image": pygame.transform.scale(pygame.image.load("assets/images/foguinho.png").convert_alpha(), (30,30)),
                "img_estatica": pygame.transform.scale(pygame.image.load("assets/images/defesa_bibs.jpg").convert_alpha(), (self.width_of_grid, self.height_of_grid)),
                "gif": "assets/gifs/bibs_atirando.gif",
            },
            {
                "index": 3,
                "price": 100,
                "shot_interval": 1000000000,
                "health": 21,
                "damage": 0,
                "bullet_image": pygame.transform.scale(pygame.image.load("assets/images/foguinho.png").convert_alpha(), (25,25)),
                "img_estatica": pygame.transform.scale(pygame.image.load("assets/images/Red_Bull.png").convert_alpha(), (self.width_of_grid, self.height_of_grid)),
                "gif": "assets/images/Red_Bull.png",
            }
        ]



    def update(self, enemies):
        self.update_towers(enemies)
        self.update_bullets(enemies)
        self.update_coins()
        self.update_life(enemies)


    def draw(self, screen):
        # Desenha prévia da Torre
        x, y = pygame.mouse.get_pos()
        allowed, x_ret, y_ret = self.grid.retify_to_grid(x, y)
        index_defesa = self.hud.selected_defense_index

        if allowed and self.money >= self.defenses[index_defesa]["price"]:
            # pygame.draw.rect(screen, self.color, (x_ret, y_ret, w, h))
            screen.blit(self.defenses[index_defesa]["img_estatica"], (x_ret, y_ret))
            screen.blit(self.surface_transparent, (x_ret, y_ret))


        # Desenha todas as torres do jogo
        for tower in self.towers:
            tower.draw(screen)
        # Desenha todas as balas do jogo
        for bullet in self.bullets:
            if bullet.active:
                screen.blit(bullet.image, (bullet.x, bullet.y))
            

    def update_towers(self, enemies):
        current_time = pygame.time.get_ticks()
        
        # Verifica se acrescenta nova torre no jogo
        # self.last_mouse_click  = pygame.mouse.get_pressed()
        if pygame.mouse.get_pressed()[0]:  # Botão esquerdo do mouse
            if current_time - self.last_click_time > DEBOUNCE_INTERVAL:
                x, y = pygame.mouse.get_pos()
                allowed, x_ret, y_ret = self.grid.retify_to_grid(x, y)
                

                index_defesa = self.hud.selected_defense_index

                if allowed and self.money >= self.defenses[index_defesa]["price"]:
                    # background_image = pygame.image.load("assets/images/prantinha.gif").convert_alpha()  # Atualize com o caminho correto para sua imagem
                    # background_image = pygame.transform.scale(background_image, (self.width_of_grid, self.height_of_grid))  # Ajusta a imagem ao tamanho da tela
                    new_tower = Tower(x_ret, y_ret, self.width_of_grid, self.height_of_grid, self.defenses[index_defesa]["health"], self.defenses[index_defesa]["shot_interval"], self.defenses[index_defesa]["gif"],self.defenses[index_defesa]["damage"],  self.defenses[index_defesa]["bullet_image"])
                    # new_tower = Tower(x_ret, y_ret, self.width_of_grid, self.height_of_grid, 20, "assets/images/prantinha.gif")
                    self.money -= self.defenses[index_defesa]["price"]
                    self.hud.update_money(self.money)
                    self.towers.append(new_tower)
                    self.grid.celula_ocupar(x, y)
                    self.last_click_time = current_time

        # faz update da torre, mudando estado e atirando
        for tower in self.towers[:]:
            # verifica se a torre morreu/está inativa
            if not tower.active:
                self.towers.remove(tower)
                self.grid.limpar_celula(tower.x, tower.y)
            else:
                if tower.verify_to_shoot(enemies):
                    tower.update()
                # Tenta atirar se tiver passado o intervalo de tempo
                bullet = tower.try_to_shoot(current_time, enemies)
                if bullet:
                    self.bullets.append(bullet)
                

    def update_bullets(self, enemies):
        for bullet in self.bullets[:]:  # Usar cópia da lista para segurança na iteração
            bullet.update(enemies)
        # Filtra a lista de balas para manter apenas as que estão ativas
        self.bullets = [bullet for bullet in self.bullets if bullet.active]


    def remove_bullet(self, bullet):
        if bullet in self.bullets:
            self.bullets.remove(bullet)
            

    def update_coins(self):
        pass


    def update_life(self, enemies):
        for enemy in enemies:
            if enemy.x < 10:
                self.life -= 1
                self.hud.update_life(self.life)
                enemies. remove(enemy)
        if self.life <= 0:
            self.game_over()

    def game_over(self):
        self.menu.game_over = True