import pygame
from os import path
from constantes import *

# # Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'assets/img')

# Carrega todos os assets de uma vez.
def load_assets(img_dir):
    assets = {}
    assets[PLAYER_IMG_FOGO] = pygame.image.load(path.join(img_dir,'players/Fireboy_em_pe.png')).convert_alpha()
    assets[PLAYER_IMG_FOGO_RUN] = pygame.image.load(path.join(img_dir,'players/Fireboy_correndo.png')).convert_alpha()
    assets[PLAYER_IMG_FOGO_RUN_ESQ] = pygame.image.load(path.join(img_dir,'players/Fireboy_correndo_esq.png')).convert_alpha()
    assets[PLAYER_IMG_AGUA] = pygame.image.load(path.join(img_dir,'players/Watergirl_em_pe.png')).convert_alpha()
    assets[PLAYER_IMG_AGUA_RUN] = pygame.image.load(path.join(img_dir,'players/Watergirl_correndo.png')).convert_alpha()
    assets[PLAYER_IMG_AGUA_RUN_ESQ] = pygame.image.load(path.join(img_dir,'players/Watergirl_correndo_esquerda.png')).convert_alpha()
    assets[BLOCK] = pygame.image.load(path.join(img_dir,'blocos_plataforma/bloco_padrao.png')).convert()
    assets[AGUA] = pygame.image.load(path.join(img_dir,'blocos_plataforma/bloco_agua.png')).convert()
    assets[FOGO] = pygame.image.load(path.join(img_dir,'blocos_plataforma/bloco_fogo.png')).convert()
    assets[VENENO] = pygame.image.load(path.join(img_dir,'blocos_plataforma/bloco_veneno.png')).convert()
    assets[INITIAL_FABRIC] = pygame.image.load(path.join(img_dir,'fundo_tela_inicial.png')).convert()
    assets[GAME_OVER] = pygame.transform.scale(pygame.image.load(path.join(img_dir,'GAME_OVER.png')),(WIDTH,HEIGHT)).convert()
    assets[PORTA_FOGO] = pygame.image.load(path.join(img_dir,'blocos_plataforma/porta_fogo.jpeg')).convert()
    assets[PORTA_AGUA] = pygame.image.load(path.join(img_dir,'blocos_plataforma/porta_agua.jpeg')).convert()
    assets[VITORIA] = pygame.image.load(path.join(img_dir,'TELA_VITORIA.png')).convert()
    return assets

#TELA INICIAL DO JOGO:
def fog_water_start(tela):

    #carrega assets:
    assets = load_assets(img_dir)
    pygame.mixer.init()

    clock = pygame.time.Clock()

    #carrega imagens:
    tela_inicial = assets[INITIAL_FABRIC] 
    tela_inicial_rect = tela_inicial.get_rect()

    #verifica se vai sair do jogo:
    joga = True
    while joga:
        state = INIT
        clock.tick(FPS)

        for event in pygame.event.get():
        # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
                joga = False     
            #Verifica se o jogo vai iniciar:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    state = PLAYING
                    joga = False
        
        #desenha:
        tela.blit(tela_inicial,tela_inicial_rect)
        pygame.display.flip()
    return state


def game_over(fundo):
    #carrega assets:
    assets = load_assets(img_dir)

    clock = pygame.time.Clock()
    clock.tick(FPS)

    #carrega imagem:
    dead = assets[GAME_OVER] 
    tela_dead_rect = dead.get_rect()
    funciona = True
    restart = False

    #verifica se fecha o jogo:
    while funciona:
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    funciona = False
                    restart = True
                if event.key == pygame.K_ESCAPE:
                    return False
            
        #atualiza tela:
        fundo.fill(BLACK)
        fundo.blit(dead, tela_dead_rect)
        pygame.display.flip()

    clock.tick(FPS)
            
    return restart 

#DEFINE A FUNÇÃO DE VITÓRIA DO JOGO:
def vitoria(fundo):
    # Carrega assets:
    assets = load_assets(img_dir)

    clock = pygame.time.Clock()
    clock.tick(FPS)

    # Carrega imagem de vitória:
    vitoria_img = assets[VITORIA]  
    tela_vitoria_rect = vitoria_img.get_rect()
    funciona = True
    continuar = False  # Variável para controlar se o jogador quer continuar jogando

    # Verifica se fecha o jogo:
    while funciona:
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:  # Verifica se o jogador clicou no botão "X"
                return False  # Sai da função e do jogo
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    funciona = False
                    continuar = True  # Se o jogador pressionar Enter, ele quer continuar
                if event.key == pygame.K_ESCAPE:
                    return False

        # Atualiza tela:
        fundo.fill(BLACK)  # Define a cor de fundo da tela
        fundo.blit(vitoria_img, tela_vitoria_rect)  # Desenha a imagem de vitória
        pygame.display.flip()  # Atualiza a tela

    clock.tick(FPS)

    return continuar  # Retorna se o jogador quer continuar jogando