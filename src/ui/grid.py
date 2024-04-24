import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Grid:
    def __init__(self, borda_sup, borda_lat, num_of_lines, num_of_columns):
        # Definição do grid
        self.matriz_ocupacao = [[False] * 5 for _ in range(9)]
        # Parâmetros do retângulo
        self.x_inicial = borda_lat
        self.largura = SCREEN_WIDTH - 2*borda_lat
        self.y_inicial = borda_sup
        self.altura = SCREEN_HEIGHT - borda_sup
        self.num_of_lines = num_of_lines
        self.num_of_columns = num_of_columns

        # Definição de cores
        self.verde_escuro = (34, 139, 34)
        self.preto = (0, 0, 0)

        # Colocando imagem de fundo
        self.background_image_2 = pygame.image.load("assets/images/background_map.png")
        self.background_image_2 = pygame.transform.scale(self.background_image_2, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_image = pygame.image.load("assets/images/grama.png")  
        self.background_image = pygame.transform.scale(self.background_image, (self.largura, self.altura))  

    def desenhar_fundo(self, screen):
        screen.blit(self.background_image_2, (0,0))
        screen.blit(self.background_image, (self.x_inicial, self.y_inicial))

    # Verificar se a celula está vazia
    def verificar_celula_ocupada(self, linha, coluna):
        if self.matriz_ocupacao[linha][coluna] == False:
            return False
        else:
            return True

    # Ocupar a célula
    def celula_ocupar(self, x, y):
        linha = int((x - self.x_inicial) // (self.largura/self.num_of_columns)) #(x - self.x_inicial) // 60
        coluna = int((y - self.y_inicial) // (self.altura/self.num_of_lines)) #(y - self.y_inicial) // 60
        self.matriz_ocupacao[linha][coluna] = True
    
    # Limpar célula específica
    def limpar_celula(self, x, y):
        linha = int((x - self.x_inicial + 1) // (self.largura/self.num_of_columns)) # o mais 1 serve pra corrigir a aproximação
        coluna = int((y - self.y_inicial + 1) // (self.altura/self.num_of_lines)) #o mais 1 serve pra corrigir a aproximação
        self.matriz_ocupacao[linha][coluna] = False

    # Reinicia a matriz para o inicio
    def limpar_matriz(self):
        self.matriz_ocupacao = [[False] * 5 for _ in range(9)]
        
    def retify_to_grid(self, x, y):
        quociente_x = int((x - self.x_inicial) // (self.largura/self.num_of_columns)) #(x - self.x_inicial) // 60
        quociente_y = int((y - self.y_inicial) // (self.altura/self.num_of_lines)) #(y - self.y_inicial) // 60
        x_grid = self.x_inicial + (self.largura/self.num_of_columns)*quociente_x
        y_grid = self.y_inicial + (self.altura/self.num_of_lines)*quociente_y

        in_screen = self.x_inicial <= x <= self.x_inicial + self.largura and self.y_inicial <= y <= self.y_inicial + self.altura
        if in_screen and not self.verificar_celula_ocupada(quociente_x, quociente_y):
            return True, x_grid, y_grid
        return False, x_grid, y_grid
