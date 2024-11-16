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
    assets[VITORIA] = pygame.transform.scale(pygame.image.load(path.join(img_dir,'TELA_VITORIA.png')),(WIDTH,HEIGHT)).convert()
    assets[DIAMANTE_A] =  pygame.image.load(path.join(img_dir,'blocos_plataforma/DIAMANTE_AGUA.png')).convert()
    assets[DIAMANTE_F] =  pygame.image.load(path.join(img_dir,'blocos_plataforma/DIAMANTE_FOGO.png')).convert()
    assets[VITORIA_1] = pygame.transform.scale(pygame.image.load(path.join(img_dir,'VICTORY_1_STAR.png')),(WIDTH,HEIGHT)).convert()
    assets[VITORIA_2] = pygame.transform.scale(pygame.image.load(path.join(img_dir,'VICTORY_2_STARS.png')),(WIDTH,HEIGHT)).convert()
    assets[VITORIA_3] = pygame.transform.scale(pygame.image.load(path.join(img_dir,'VICTORY_3_STARS.png')),(WIDTH,HEIGHT)).convert()
    return assets

#TELA INICIAL DO JOGO:
def fog_water_start(tela):

    #carrega assets:
    assets = load_assets(img_dir)
    pygame.mixer.init()
    pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
    pygame.mixer.music.set_volume (2.0)
    pygame.mixer.music.play (-1)

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

# DEFINE A FUNÇÃO DE VITÓRIA DO JOGO:
def vitoria(fundo, scores_agua, scores_fogo):
    # Carrega assets:
    assets = load_assets(img_dir)
    pygame.mixer.init()
    pygame.mixer.music.load('assets/som/SOM_VITORIA.mp3')
    pygame.mixer.music.set_volume (2.0)
    pygame.mixer.music.play (-1)

    clock = pygame.time.Clock()
    clock.tick(FPS)

    # Define as imagens de vitória com base na soma dos scores
    total_scores = scores_agua + scores_fogo
    if total_scores == 0:
        vitoria_img = assets[VITORIA]  # Imagem para scores baixos
    elif 0 < total_scores <= 600 :
        vitoria_img = assets[VITORIA_1]  # Imagem para scores médios
    elif 600 < total_scores <= 1200:
        vitoria_img = assets[VITORIA_2]  # Imagem para scores altos
    else:
        vitoria_img = assets[VITORIA_3]  # Imagem para scores máximos

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