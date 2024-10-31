from pathlib import Path


# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = Path(__file__).parent / 'assets/img/blocos_plataforma'

# Dados gerais do jogo.
TITULO = 'FASE 1'
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
MAPA = [
    [BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM],
    [BLOCO_MARROM, PORTA_AGUA__, PORTA_FOGO__, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, BLOCO_MARROM],
    [BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, NADA________, NADA________, BLOCO_MARROM],
    [BLOCO_MARROM, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, BLOCO_MARROM, BLOCO_MARROM],
    [BLOCO_MARROM, NADA________, NADA________, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM],
    [BLOCO_MARROM, BLOCO_MARROM, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, BLOCO_MARROM],
    [BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, NADA________, NADA________, BLOCO_MARROM],
    [BLOCO_MARROM, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, BLOCO_MARROM, BLOCO_MARROM],
    [BLOCO_MARROM, BLOCO_MARROM, NADA________, NADA________, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM],
    [BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM],
    [BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, NADA________, NADA________, NADA________, DIA_MARROM_E, BLOCO_MARROM],
    [BLOCO_MARROM, NADA________, NADA________, NADA________, NADA________, DIA_MARROM_E, BLOCO_MARROM, BLOCO_MARROM, NADA________, NADA________, NADA________, BLOCO_MARROM],
    [BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, BLOCO_MARROM, BLOCO_MARROM],
    [BLOCO_MARROM, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, NADA________, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM],
    [BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM, BLOCO_MARROM],
]
