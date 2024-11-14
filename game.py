import pygame
from constantes import *
from classes import *
from utils import *
from fases import *
import time

#LOOP DO JOGO PRINCIPAL:
def game_screen(screen):
    
    state = INIT

    while state != DONE:
        if state == INIT:
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            state = fog_water_start(screen)
        elif state == PLAYING:
            state = fase1(screen)
        elif state == HOME2:
            state = fase2(screen)
        elif state == HOME3:
            state = fase3(screen)
        else:
            state = DONE


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()

# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Nome do jogo
pygame.display.set_caption(TITULO)

# Imprime instruções
print('*' * len(TITULO))
print(TITULO.upper())
print('*' * len(TITULO))
print('Utilize as setas do teclado para andar e pular.')

# Comando para evitar travamentos.
try:
    game_screen(screen)
finally:
    pygame.quit()