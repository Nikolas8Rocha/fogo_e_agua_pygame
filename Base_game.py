# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from jogo_sem_classes import *
from plataformas import *

pygame.init()
WIDTH = 1400 #largura da tela
HEIGHT = 700 #altura da tela
# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo do Pedro')

# ----- Inicia estruturas de dados
Inicio = 0
Jogando_nivel_1 = 1
state = Inicio
game = True
background_inicial = pygame.image.load("assets/img/tela_fundo_inicial.png").convert()
background_inicial = pygame.transform.scale(background_inicial,(WIDTH,HEIGHT))
background_jogando_1 = pygame.image.load("assets/img/fundo_niveis.png").convert()
background_jogando_1 = pygame.transform.scale(background_jogando_1,(WIDTH,HEIGHT))


# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        
        if event.type == pygame.QUIT:
            game = False     
#Verifica se o jogo vai iniciar:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                state = Jogando_nivel_1
    if state == Inicio:
        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(background_inicial,(0,0))
    if state == Jogando_nivel_1:
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(background_jogando_1,(0,0))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
