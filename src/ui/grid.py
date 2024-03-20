import pygame
from src.settings import SCREEN_WIDTH

class Grid:
    def __init__(self):
        # Definição do grid
        self.matriz_ocupacao = [[False] * 12 for _ in range(8)]

        # Parâmetros do retângulo
        self.x_inicial = 0
        self.largura = SCREEN_WIDTH
        self.y_inicial = 120
        self.altura = 480

        # Definição de cores
        self.verde_escuro = (34, 139, 34)
        self.preto = (0, 0, 0)

    # Desenha o retângulo na tela
    def desenhar_retangulo(self, screen):
        pygame.draw.rect(screen, self.verde_escuro, (self.x_inicial, self.y_inicial, self.largura, self.altura))

    # Desenha as linhas do grid na tela
    def desenhar_linhas(self, screen):
        for x in range(self.x_inicial, self.x_inicial + self.largura, 60):
            pygame.draw.line(screen, self.preto, (x, 120), (x, 600))
        for y in range(self.y_inicial, 601, 60):
            pygame.draw.line(screen, self.preto, (40, y), (760, y))

    # Verificar se a celula está vazia
    def verificar_celula_ocupada(self, linha, coluna):
        if self.matriz_ocupacao[linha][coluna] == False:
            return False
        else:
            return True

    # Ocupar a célula
    def celula_ocupada(self, linha, coluna):
        self.matriz_ocupacao[linha][coluna] = True
    
    # Limpar célula específica
    def limpar_celula(self, linha, coluna):
        self.matriz_ocupacao[linha][coluna] = False

    # Reinicia a matriz para o inicio
    def limpar_matriz(self):
        self.matriz_ocupacao = [[False] * 6 for _ in range(4)]

    def retify_to_grid(self, x, y):
        resto_x = (x - self.x_inicial) // 60
        resto_y = (y - self.y_inicial) // 60
        x_grid = self.x_inicial + 60*resto_x
        y_grid = self.y_inicial + 60*resto_y
        return x_grid, y_grid
