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

background_inicial = pygame.image.load("assets/img/fundo_tela_inicial.png").convert()
background_inicial = pygame.transform.scale(background_inicial,(LARGURA ,ALTURA))
background_jogando_1 = pygame.image.load("assets/img/fundo_niveis.png").convert()
background_jogando_1 = pygame.transform.scale(background_jogando_1,(LARGURA ,ALTURA))
background_morreu = pygame.image.load("assets/img/GAME_OVER.png").convert()
background_morreu = pygame.transform.scale(background_morreu,(LARGURA ,ALTURA))

fogo = pygame.image.load('assets/img/players/Fireboy_em_pe.png').convert_alpha()
fogo = pygame.transform.scale(fogo, (LARGURA_QUADRADO-5, ALTURA_QUADRADO-5))
agua = pygame.image.load('assets/img/players/Watergirl_em_pe.png').convert_alpha()
agua = pygame.transform.scale(agua, (LARGURA_QUADRADO-5, ALTURA_QUADRADO-5))

class posicao_fogo(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()

        self.rect.left = TAMANHO_QUADRADO
        self.rect.bottom = ALTURA - TAMANHO_QUADRADO

        self.speedx = 0
        self.speedy = 0
    
    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0

class posicao_agua(pygame.sprite.Sprite):
    def __init__(self, img):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()

        self.rect.left = TAMANHO_QUADRADO*2
        self.rect.bottom = ALTURA - TAMANHO_QUADRADO

        self.speedx = 0
        self.speedy = 0
    
    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        if self.rect.left < 0:
            self.rect.left = 0




fase = 'tela_inicial'
player_fogo = posicao_fogo(fogo)
player_agua = posicao_agua(agua)

all_players = pygame.sprite.Group()
all_players.add(player_fogo)
all_players.add(player_agua)
pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
pygame.mixer.music.set_volume (1.0)
pygame.mixer.music.play (-1)
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
                    pygame.mixer.music.load('assets/som/In_game.mp3')
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.play(-1)
            
    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
        all_players.update()

            # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(background_inicial,(0,0))

    if fase == 'nivel1':
        assets = jsc.teste()
        jsc.game_loop(window, assets)

        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
        
        # Verifica se apertou alguma tecla e mexe o fogo.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player_fogo.speedx -= 4
                if event.key == pygame.K_RIGHT:
                    player_fogo.speedx += 4
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player_fogo.speedx += 4
                if event.key == pygame.K_RIGHT:
                    player_fogo.speedx -= 4
            
        # Verifica se apertou alguma tecla e mexe a água.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_a:
                    player_agua.speedx -= 4
                if event.key == pygame.K_d:
                    player_agua.speedx += 4
            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera a velocidade.
                if event.key == pygame.K_a:
                    player_agua.speedx += 4
                if event.key == pygame.K_d:
                    player_agua.speedx -= 4    

        #atualiza grupo de jogadores:
        all_players.update()

         # Verifica se houve colisão entre bala e meteoro:
        # hits = pygame.sprite.groupcollide(all_players,all_bloco, False,False)
        # if len(hits) > 0:
        
        """for bloco in all_bloco.sprites():
            print(bloco.rect)
            if player_agua.rect.colliderect(bloco.rect):
                print( 'parede aaaa')
                if player_agua.rect.midright > bloco.rect.midleft:
                    print('parede')""" 

        all_players.draw(window)

        # window.fill(janela)  # Preenche com a cor branca
    if fase == "morreu":
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(background_morreu,(0,0))
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False     
    #Verifica se o jogo vai iniciar:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game = False  
                if event.key == pygame.K_RETURN:
                    fase = 'nivel1'
                    pygame.mixer.music.load('assets/som/In_game.mp3')
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.play(-1)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados