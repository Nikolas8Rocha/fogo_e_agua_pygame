# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import jogo_sem_classes as jsc
from constantes2 import *

pygame.init()
# ----- Gera tela principal
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo Fogo e Água')


# ----- Inicia estruturas de dados
game = True

background_inicial = pygame.image.load("assets/img/tela_fundo_inicial.png").convert()
background_inicial = pygame.transform.scale(background_inicial,(LARGURA ,ALTURA))
background_jogando_1 = pygame.image.load("assets/img/fundo_niveis.png").convert()
background_jogando_1 = pygame.transform.scale(background_jogando_1,(LARGURA ,ALTURA))

#mapa1 = 

fase = 'tela_inicial'
# fase = 'nivel1'
# ===== Loop principal =====
while game:
    if fase == 'tela_inicial':
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False     
    #Verifica se o jogo vai iniciar:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    fase = 'nivel1'
            # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(background_inicial,(0,0))

    if fase == 'nivel1':
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
        FUNDO = background_jogando_1
        #window.blit(background_jogando_1,(0,0))

        assets = jsc.teste()
        jsc.game_loop(window, assets, FUNDO)
        # window.fill(janela)  # Preenche com a cor branca

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados