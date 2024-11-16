import pygame
from constantes import *
from classes import *
from utils import *
from fase1 import *
from fase2 import *
from fase3 import *


#LOOP DO JOGO PRINCIPAL:
def game_screen(screen):
    
    state = INIT
    score_agua = 0
    score_fogo = 0
    while state != DONE:
        if state == INIT:
            screen = pygame.display.set_mode((WIDTH, HEIGHT))
            state = fog_water_start(screen)
        elif state == PLAYING:
            state, scores = fase1(screen,score_agua, score_fogo)
            score_agua, score_fogo = scores
        elif state == HOME2:
            state, scores = fase2(screen,score_agua, score_fogo)
            score_agua, score_fogo = scores
        elif state == HOME3:
            state, scores = fase3(screen,score_agua, score_fogo)
            score_agua, score_fogo = scores
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