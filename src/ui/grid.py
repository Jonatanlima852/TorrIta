import pygame
from src.settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Grid:
    def __init__(self, borda_sup, borda_lat, num_of_lines, num_of_columns):
        # Definição do grid
        self.matriz_ocupacao = [[False] * 9 for _ in range(5)]
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

    # Desenha o retângulo na tela
    def desenhar_retangulo(self, screen):
        pygame.draw.rect(screen, self.verde_escuro, (self.x_inicial, self.y_inicial, self.largura, self.altura))

    # Desenha as linhas do grid na tela
    def desenhar_linhas(self, screen):
        #for x in range(self.x_inicial, self.largura, int(self.largura//self.num_of_lines)):
        for k in range(0, self.num_of_columns):
            x = self.x_inicial + k * self.largura//self.num_of_columns
            pygame.draw.line(screen, self.preto, (x, self.y_inicial), (x, self.altura + self.y_inicial))
            
        for k in range(0, self.num_of_lines):
            y = self.y_inicial + k * self.altura//self.num_of_lines
        #for y in range(self.y_inicial, int(self.altura , int(self.altura//self.num_of_columns)):
            pygame.draw.line(screen, self.preto, (self.x_inicial, y), (self.x_inicial + self.largura, y))

    # Verificar se a celula está vazia
    def verificar_celula_ocupada(self, linha, coluna):
        if self.matriz_ocupacao[linha][coluna] == False:
            return False
        else:
            return True

    # Ocupar a célula
    def celula_ocupar(self, linha, coluna):
        self.matriz_ocupacao[linha][coluna] = True
    
    # Limpar célula específica
    def limpar_celula(self, linha, coluna):
        self.matriz_ocupacao[linha][coluna] = False

    # Reinicia a matriz para o inicio
    def limpar_matriz(self):
        self.matriz_ocupacao = [[False] * 9 for _ in range(5)]
    
    # Analisa se o click foi em uma posição válida e altera a função célula ocupada
    def Posicao_click(self, x, y):
        if x in range(40, 761) and y in range(120, 601):
            posicao_x = (x - 40) // 120
            posicao_y = (y - 120) // 80
            self.celula_ocupar(posicao_y, posicao_x)

            return True, posicao_x, posicao_y
        else:
            return False
        
    def retify_to_grid(self, x, y):
        resto_x = (x - self.x_inicial) // (self.largura/self.num_of_columns) #(x - self.x_inicial) // 60
        resto_y = (y - self.y_inicial) // (self.altura/self.num_of_lines) #(y - self.y_inicial) // 60
        x_grid = self.x_inicial + (self.largura/self.num_of_columns)*resto_x
        y_grid = self.y_inicial + (self.altura/self.num_of_lines)*resto_y
        if self.x_inicial <= x <= self.x_inicial + self.largura and self.y_inicial <= y <= self.y_inicial + self.altura:
            return True, x_grid, y_grid
        return False, x_grid, y_grid
