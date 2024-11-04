# -*- coding: utf-8 -*-

# Importando as bibliotecas necessárias.
import pygame
from pathlib import Path
from constantes2 import *


def teste():

    # Cada tile é uma imagem quadrada de TAMANHO_QUADRADO x TAMANHO_QUADRADO pixels.
    assets = {
        BLOCO_MARROM: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_marrom_grande.png'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        BLOCO_PRETO_: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_preto_grande.png'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        DIA_MARROM_D: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_marrom_diagonal_direita.png'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        DIA_MARROM_E: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_marrom_diagonal_esquerda.png'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        DIA_PRETO_D_: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_preto_diagonal_direita.png'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        DIA_PRETO_E_: pygame.transform.scale(pygame.image.load(IMG_DIR / 'bloco_preto_diagonal_esquerda.png'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        PORTA_AGUA__: pygame.transform.scale(pygame.image.load(IMG_DIR / 'porta_agua.jpeg'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        PORTA_FOGO__: pygame.transform.scale(pygame.image.load(IMG_DIR / 'porta_fogo.jpeg'), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        LQD_VENENO__: pygame.transform.scale(pygame.image.load(IMG_DIR / 'veneno_chao.png').convert_alpha(), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        LQD_AGUA____: pygame.transform.scale(pygame.image.load(IMG_DIR / 'agua_chao.png').convert_alpha(), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        LQD_FOGO____: pygame.transform.scale(pygame.image.load(IMG_DIR / 'fogo_chao.png').convert_alpha(), (LARGURA_QUADRADO, ALTURA_QUADRADO)),
        'mapa_tiles': MAPA,
    }

    return assets




def game_loop(janela, assets):
    desenha(janela, assets)


def desenha(janela, assets):
    # A cada frame, redesenha o fundo e os sprites
    #janela.blit(fundo, (0,0))
    janela.fill(PRETO)

    for linha in range(len(assets['mapa_tiles'])):
        for coluna in range(len(assets['mapa_tiles'][linha])):
            tipo_quadrado = assets['mapa_tiles'][linha][coluna]
            if tipo_quadrado != NADA________:
                janela.blit(assets[tipo_quadrado], (TAMANHO_QUADRADO * coluna, TAMANHO_QUADRADO * linha))

    # pygame.display.update()




