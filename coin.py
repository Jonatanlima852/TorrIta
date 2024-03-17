import pygame
import sys
import random

# Inicializar o Pygame
pygame.init()

# Definir o tamanho da janela
largura, altura = 600, 600

# Definir o tamanho do grid
num_colunas = 10
num_linhas = 6

largura_coluna = largura // num_colunas
altura_linha = altura // num_linhas

# Definir as cores
BRANCO = (0, 0, 0)

# Criar a janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Moedas Caindo")

# Carregar a imagem da moeda
moeda_img = pygame.image.load('coin.png')
moeda_img = pygame.transform.scale(moeda_img, (60, 60))

# Definir lista para armazenar as moedas
moedas = []

# Variável para armazenar a quantidade de dinheiro
dinheiro = 0

# Fonte para exibir o dinheiro
fonte = pygame.font.SysFont(None, 36)

# Lista de posições onde as moedas podem aparecer no topo da tela
posicoes = [largura_coluna * i + largura_coluna // 2 for i in range(num_colunas - 1)]

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_rect = pygame.Rect(mouse_pos[0], mouse_pos[1], 1, 1)  # Criar um retângulo para representar o ponto do mouse
            print( mouse_pos  )
            for moeda in moedas:
                if moeda['retangulo'].colliderect(mouse_rect):
                    print("foi removida a moeda")
                    moedas.remove(moeda)  # Remover a moeda clicada
                    dinheiro += 10  # Incrementar o valor do dinheiro


    # Preencher a janela com a cor branca
    janela.fill(BRANCO)

    # Adicionar nova moeda aleatoriamente no topo da tela
    if random.randint(0, 100) < 2:  # Chance de 2% de uma nova moeda aparecer
        coluna = random.choice(posicoes)
        nova_moeda = {'x': coluna, 'y': 0}  # Começa acima da tela para cair
        # Definir a posição final da moeda dentro da coluna
        nova_moeda['y_final'] = random.randint(0, altura_linha * num_linhas - 60)
        nova_moeda['retangulo'] = pygame.Rect(nova_moeda['x'], nova_moeda['y'], 50, 50)
        moedas.append(nova_moeda)

    # Atualizar a posição das moedas
    for moeda in moedas:
        if moeda['y'] < moeda['y_final']:  # Se a moeda não atingiu sua posição final
            moeda['y'] += 1  # Velocidade de queda da moeda
            moeda['retangulo'].y = moeda['y']
        janela.blit(moeda_img, (moeda['x'], moeda['y']))

    # Desenhar o valor do dinheiro na tela
    texto = fonte.render(f'Dinheiro: {dinheiro}', True, (255, 255, 255))
    janela.blit(texto, (10, 10))

    # Atualizar a tela
    pygame.display.flip()

    # Controlar a taxa de atualização da tela
    pygame.time.Clock().tick(30)  # 30 FPS

