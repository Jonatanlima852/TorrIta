import pygame

class Grid:
    def __init__(self):
        # Definição do grid
        self.matriz_ocupacao = [[False] * 6 for _ in range(6)]

        # Parâmetros do retângulo
        self.x_inicial = 40
        self.largura = 720
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
        for x in range(160, 761, 120):
            pygame.draw.line(screen, self.preto, (x, 120), (x, 600))
        for y in range(120, 601, 80):
            pygame.draw.line(screen, self.preto, (40, y), (760, y))

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
        self.matriz_ocupacao = [[False] * 6 for _ in range(6)]
    
    # Analisa se o click foi em uma posição válida e altera a função célula ocupada
    def Posicao_click(self, x, y):
        if x in range(40, 761) and y in range(120, 601):
            posicao_x = (x - 40) // 120
            posicao_y = (y - 120) // 80
            self.celula_ocupar(posicao_y, posicao_x)

            return True, posicao_x, posicao_y
        else:
            return False