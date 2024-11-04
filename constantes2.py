from pathlib import Path

import pygame




# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = Path(__file__).parent / 'assets/img/blocos_plataforma'

# Dados gerais do jogo.

LARGURA = 480 # Largura da tela
ALTURA = 600 # Altura da tela
TAMANHO_QUADRADO = 40 # Tamanho de cada quadrado (tile)
ALTURA_QUADRADO = 40
LARGURA_QUADRADO = 40
# Define algumas variáveis com as cores básicas
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VEMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (255, 255, 0)


# Define os tipos de tiles
# Os underscores no final são apenas para manter todas as variáveis com o mesmo tamanho.
BLOCO_MARROM = 0
BLOCO_PRETO_ = 1
LQD_VENENO__ = 2 # LQD = LIQUÍDO
LQD_AGUA____ = 3
LQD_FOGO____ = 4
DIA_MARROM_D = 5 # DIA = DIAGONAL  --- D = direita ---- E = esquerda
DIA_MARROM_E = 6 # 
DIA_PRETO_D_ = 7
DIA_PRETO_E_ = 8
PORTA_AGUA__ = 9 
PORTA_FOGO__ = 10
NADA________ = 11






# Define o mapa com os tipos de tiles    
TITULO = 'FASE 1'
MAPA = [
    [BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM],
    [BLOCO_MARROM, PORTA_AGUA__, PORTA_FOGO__, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, BLOCO_MARROM],
    [BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, LQD_VENENO__, NADA________, NADA________, BLOCO_MARROM],
    [BLOCO_MARROM, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, BLOCO_MARROM, BLOCO_MARROM],
    [BLOCO_MARROM, NADA________, NADA________, LQD_VENENO__, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM],
    [BLOCO_MARROM, BLOCO_MARROM, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, BLOCO_MARROM],
    [BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, NADA________, NADA________, BLOCO_MARROM],
    [BLOCO_MARROM, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, BLOCO_MARROM, BLOCO_MARROM],
    [BLOCO_MARROM, BLOCO_MARROM, NADA________, NADA________, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, LQD_FOGO____, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM],
    [BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM],
    [BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, NADA________, NADA________, NADA________, DIA_MARROM_E, BLOCO_MARROM],
    [BLOCO_MARROM, NADA________, NADA________, NADA________, NADA________, DIA_MARROM_E, BLOCO_MARROM, BLOCO_MARROM, NADA________, NADA________, NADA________, BLOCO_MARROM],
    [BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, BLOCO_MARROM, BLOCO_MARROM],
    [BLOCO_MARROM, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM],
    [BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, LQD_AGUA____, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM],
]

class blocos (pygame.sprite.Sprite):
    def __init__(self, nome, posicao):
        pygame.sprite.Sprite.__init__(self)

        

        assets = {
        BLOCO_MARROM: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_marrom_grande.png'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        BLOCO_PRETO_: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_preto_grande.png'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        DIA_MARROM_D: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_marrom_diagonal_direita.png'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        DIA_MARROM_E: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_marrom_diagonal_esquerda.png'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        DIA_PRETO_D_: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_preto_diagonal_direita.png'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        DIA_PRETO_E_: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_preto_diagonal_esquerda.png'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        PORTA_AGUA__: pygame.transform.scale(pygame.image.load(IMG_DIR / 'porta_agua.jpeg'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        PORTA_FOGO__: pygame.transform.scale(pygame.image.load(IMG_DIR / 'porta_fogo.jpeg'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        LQD_VENENO__: pygame.transform.scale(pygame.image.load(IMG_DIR / 'veneno_chao.png'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        LQD_AGUA____: pygame.transform.scale(pygame.image.load(IMG_DIR / 'agua_chao.png'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        LQD_FOGO____: pygame.transform.scale(pygame.image.load(IMG_DIR / 'fogo_chao.png'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        }

        self.img = assets[nome]
        self.posicao = posicao
        self.rect = pygame.Rect(posicao, TAMANHO_QUADRADO)
        self.nome = nome
        
        
        



all_bloco = pygame.sprite.Group()
for linha in range(len(MAPA)):
    for coluna in range(len(MAPA[linha])):
        if MAPA[linha][coluna] != NADA________:
            adicona_bloco = blocos((linha*TAMANHO_QUADRADO,coluna*TAMANHO_QUADRADO))
            all_bloco.add(adicona_bloco)