# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from constantes import *


# Classe Tile que representa um quadrado do mapa
class Tile(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, tile_img, row, column):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = TAMANHO_QUADRADO * column
        self.rect.y = TAMANHO_QUADRADO * row


def inicializa():
    pygame.init()

    janela = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption(TITULO)

    # Cada tile é uma imagem quadrada de TILE_SIZE x TILE_SIZE pixels.
    assets = {
        BLOCO_MARROM: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_marrom_grande.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        BLOCO_PRETO_: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_preto_grande.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        LQD_VENENO__: pygame.transform.scale(pygame.image.load(IMG_DIR / 'principal.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        LQD_AGUA____: pygame.transform.scale(pygame.image.load(IMG_DIR / 'principal.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        LQD_FOGO____: pygame.transform.scale(pygame.image.load(IMG_DIR / 'principal.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        DIA_MARROM_D: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_marrom_diagonal_direita.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        DIA_MARROM_E: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_marrom_diagonal_esquerda.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        DIA_PRETO_D_: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_preto_diagonal_direita.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        DIA_PRETO_E_: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_preto_diagonal_esquerda.png'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        PORTA_AGUA__: pygame.transform.scale(pygame.image.load(IMG_DIR / 'porta_agua.jpeg'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
        PORTA_FOGO__: pygame.transform.scale(pygame.image.load(IMG_DIR / 'porta_fogo.jpeg'), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)),
    }
    # Cria um grupo de tiles.
    mapa_tiles = pygame.sprite.Group()
    # Cria tiles de acordo com o mapa
    for linha in range(len(MAPA)):
        for coluna in range(len(MAPA[linha])):
            tipo_quadrado = MAPA[linha][coluna]
            if tipo_quadrado != NADA________:
                quadrado = Tile(assets[tipo_quadrado], linha, coluna)
                mapa_tiles.add(quadrado)
    assets['mapa_tiles'] = mapa_tiles

    return janela, assets


def atualiza_estado():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True


def game_loop(janela, assets):
    while atualiza_estado():
        desenha(janela, assets)


def desenha(janela, assets):
    # A cada frame, redesenha o fundo e os sprites
    janela.fill(PRETO)
    assets['mapa_tiles'].draw(janela)

    pygame.display.update()


if __name__ == '__main__':
    janela, assets = inicializa()
    game_loop(janela, assets)
