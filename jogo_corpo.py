# Importando as bibliotecas necessárias.
import pygame
import random
from os import path
import time

# # Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'assets/img')

# Dados gerais do jogo.
TITULO = 'Jogo Água e Fogo'
WIDTH = 1080 # Largura da tela
HEIGHT = 640 # Altura da tela
TILE_SIZE = 40 # Tamanho de cada tile (cada tile é um quadrado)
PLAYER_WIDTH = TILE_SIZE - 10
PLAYER_HEIGHT = TILE_SIZE - 10 
FPS = 60 # Frames por segundo

#Estados
    
PLAYING = 0
DONE = 1
INIT = 2
HOME1 = 3
HOME2 = 4

# Imagens
INITIAL_FABRIC = 'assets/img/fundo_tela_inicial.png'
PLAYER_IMG_FOGO = 'assets/img/players/Fireboy_em_pe.png'
PLAYER_IMG_FOGO_RUN = 'assets/img/players/Fireboy_em_correndo.png'
PLAYER_IMG_FOGO_RUN_ESQ = 'assets/img/players/Fireboy_em_correndo_esq.png'
PLAYER_IMG_AGUA = 'assets/img/players/Watergirl_em_pe.png'
GAME_OVER = 'assets/img/players/GAME_OVER.png'
PORTA_FOGO = 'assets/img/blocos_plataforma/porta_fogo.png'


# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Define a aceleração da gravidade
GRAVITY = 0.8
# Define a velocidade inicial no pulo
JUMP_SIZE = 13.5
# Define a velocidade em x
SPEED_X = 3


# Define os tipos de tiles
BLOCK = 0
AGUA = 1
FOGO = 2
VENENO = 3

EMPTY = -1
PORTA_AGUA = -2
PORTA_FOGO = -3




# Define o mapa com os tipos de tiles
MAP = [
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, PORTA_FOGO, BLOCK],
    [BLOCK, VENENO, BLOCK, BLOCK, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, BLOCK, BLOCK, EMPTY, BLOCK],
    [BLOCK, EMPTY, EMPTY, BLOCK, FOGO, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, AGUA, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
    [BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
    [BLOCK, BLOCK, FOGO, BLOCK, EMPTY, EMPTY, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, FOGO, FOGO, BLOCK, EMPTY, BLOCK, BLOCK, VENENO, VENENO, BLOCK, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, VENENO, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, AGUA, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
    [BLOCK, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
    [BLOCK, VENENO, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, AGUA, AGUA, BLOCK, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK],
    [BLOCK, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, FOGO, FOGO, BLOCK, BLOCK, BLOCK, VENENO, VENENO, BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK],
    [BLOCK, EMPTY, PORTA_FOGO, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, AGUA, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK]
]

MAP2 = [
    [BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK,BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
    [BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, BLOCK, BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK],
    [BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, VENENO, VENENO, VENENO, VENENO, BLOCK],
    [BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
    [BLOCK, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, VENENO, VENENO, VENENO, VENENO, EMPTY, EMPTY, BLOCK, VENENO, VENENO, VENENO, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK],
    [BLOCK, VENENO, VENENO, VENENO, VENENO, VENENO, VENENO, VENENO, BLOCK, BLOCK, BLOCK, BLOCK, VENENO, VENENO, BLOCK, BLOCK, BLOCK, VENENO, VENENO, BLOCK, BLOCK, BLOCK, VENENO, BLOCK, EMPTY, EMPTY, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK],
    [BLOCK, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, BLOCK, BLOCK, BLOCK],
    [BLOCK, BLOCK, BLOCK, BLOCK, VENENO, VENENO, VENENO, BLOCK, BLOCK, BLOCK, VENENO, VENENO, VENENO, BLOCK, BLOCK, BLOCK, BLOCK, VENENO, VENENO, VENENO, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK, BLOCK]
]

# Define estados possíveis do jogador
STILL = 0
JUMPING = 1

FALLING = 2


# Class que representa os blocos do cenário
class Tile(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, tile_img, row, column):
        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Aumenta o tamanho do tile.
        tile_img = pygame.transform.scale(tile_img, (TILE_SIZE, TILE_SIZE))

        # Define a imagem do tile.
        self.image = tile_img
        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()

        # Posiciona o tile
        self.rect.x = TILE_SIZE * column
        self.rect.y = TILE_SIZE * row


# Classe Jogador que representa o herói
class Player_Fogo(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, player_img_fogo,player_img_fogo_run,player_img_fogo_run_esq, row, column, blocks, agua,veneno,portas):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.state = STILL
        self.alive = 'alive'
        self.fase = '0'

        # Ajusta o tamanho da imagem
        self.player_img_fogo = pygame.transform.scale(player_img_fogo, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.player_img_fogo_run = pygame.transform.scale(player_img_fogo_run, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.player_img_fogo_run_esq = pygame.transform.scale(player_img_fogo_run_esq, (PLAYER_WIDTH, PLAYER_HEIGHT))

        # Define a imagem do sprite. Imagem estática (não teremos animação durante o pulo):
        self.image = self.player_img_fogo

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        self.rect_run = self.image.get_rect()

        # Guarda o grupo de blocos para tratar as colisões
        self.blocks = blocks
        self.agua = agua
        self.veneno = veneno
        self.portas = portas

        # Posiciona o personagem
        # row é o índice da linha embaixo do personagem
        self.rect.x = TILE_SIZE
        self.rect.bottom = HEIGHT - TILE_SIZE

        self.speedx = 0
        self.speedy = 0
        

    # Metodo que atualiza a posição do personagem
    def update(self):
        # Vamos tratar os movimentos de maneira independente.
        # Primeiro tentamos andar no eixo y e depois no x.

        # Tenta andar em y
        # Atualiza a velocidade aplicando a aceleração da gravidade
        self.speedy += GRAVITY
        # Atualiza o estado para caindo
        if self.speedy > 0:
            self.state = FALLING
        # Atualiza a posição y
        self.rect.y += self.speedy

        # Se colidiu com algum bloco de ÁGUA, personagem morre:
        collisions = pygame.sprite.spritecollide(self, self.agua, False)
        for collision in collisions:
            if self.rect.bottom < collision.rect.top + TILE_SIZE/2:
                self.alive = 'dead'
        
        # Se colidiu com algum bloco de VENENO, personagem morre:
        collisions = pygame.sprite.spritecollide(self, self.veneno, False)
        for collision in collisions:
            if self.rect.bottom < collision.rect.top + TILE_SIZE/2:
                self.alive = 'dead'
            
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para baixo
            if self.speedy > 0:
                self.rect.bottom = collision.rect.top
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL
            # Estava indo para cima
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom
                # Se colidiu com algo, para de cair
                self.speedy = 0
                # Atualiza o estado para parado
                self.state = STILL

        # Tenta andar em x
        self.rect.x += self.speedx
        #Verifica se o velocidade em x é maior que zero, pra mudar animação:
        if self.speedx > 0:
            self.image = self.player_img_fogo_run
        elif self.speedx < 0:
            self.image = self.player_img_fogo_run_esq
        else:
            self.image = self.player_img_fogo
        # Corrige a posição caso tenha passado do tamanho da janela
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right >= WIDTH:
            self.rect.right = WIDTH - 1
        # Se colidiu com algum bloco, volta para o ponto antes da colisão
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            # Estava indo para a direita
            if self.speedx > 0:
                self.rect.right = collision.rect.left 
            # Estava indo para a esquerda
            elif self.speedx < 0:
                self.rect.left = collision.rect.right

        #Verifica se está na mesma posição jogador e porta:
        collisions = pygame.sprite.spritecollide(self, self.portas, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            if self.rect.right < collision.rect.right + 10  and self.rect.left > collision.rect.left - 10: 
                self.rect.center = collision.rect.center
                self.fase = '2'

    # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING


# Carrega todos os assets de uma vez.
def load_assets(img_dir):
    assets = {}
    assets[PLAYER_IMG_FOGO] = pygame.image.load(path.join(img_dir,'players/Fireboy_em_pe.png')).convert_alpha()
    assets[PLAYER_IMG_FOGO_RUN] = pygame.image.load(path.join(img_dir,'players/Fireboy_correndo.png')).convert_alpha()
    assets[PLAYER_IMG_FOGO_RUN_ESQ] = pygame.image.load(path.join(img_dir,'players/Fireboy_correndo_esq.png')).convert_alpha()
    assets[BLOCK] = pygame.image.load(path.join(img_dir,'blocos_plataforma/bloco_padrao.png')).convert()
    assets[AGUA] = pygame.image.load(path.join(img_dir,'blocos_plataforma/bloco_agua.png')).convert()
    assets[FOGO] = pygame.image.load(path.join(img_dir,'blocos_plataforma/bloco_fogo.png')).convert()
    assets[VENENO] = pygame.image.load(path.join(img_dir,'blocos_plataforma/bloco_veneno.png')).convert()
    assets[INITIAL_FABRIC] = pygame.image.load(path.join(img_dir,'fundo_tela_inicial.png')).convert()
    assets[GAME_OVER] = pygame.transform.scale(pygame.image.load(path.join(img_dir,'GAME_OVER.png')),(WIDTH,HEIGHT)).convert()
    assets[PORTA_FOGO] = pygame.image.load(path.join(img_dir,'blocos_plataforma/porta_fogo.jpeg')).convert()
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


def fase1(screen):
# Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    # Cria um grupo somente com os sprites de bloco.
    # Sprites de block são aqueles que impedem o movimento do jogador
    blocks = pygame.sprite.Group()
    agua = pygame.sprite.Group()
    veneno = pygame.sprite.Group()
    portas = pygame.sprite.Group()
    

    # Cria Sprite do jogador
    player = Player_Fogo(assets[PLAYER_IMG_FOGO],assets[PLAYER_IMG_FOGO_RUN],assets[PLAYER_IMG_FOGO_RUN_ESQ], 12, 2, blocks,agua,veneno,portas)

    # Cria tiles de acordo com o mapa
    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            if tile_type == BLOCK or tile_type == AGUA or tile_type == FOGO or tile_type == VENENO or tile_type == PORTA_AGUA or tile_type == PORTA_FOGO:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                if tile_type != PORTA_FOGO and tile_type!= PORTA_AGUA:
                    blocks.add(tile)
                else:
                    portas.add(tile)
            if tile_type == AGUA:
                tile = Tile(assets[tile_type], row, column)
                agua.add(tile)
            if tile_type == VENENO:
                tile = Tile(assets[tile_type], row, column)
                veneno.add(tile)
    
    # Adiciona o jogador no grupo de sprites por último para ser desenhado por
    # cima dos blocos
    all_sprites.add(player)


    state = HOME1

    if player.alive != "dead":
            pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
            pygame.mixer.music.set_volume (2.0)
            pygame.mixer.music.play (-1)
    
    while state != DONE:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():

            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE

            # # Verifica se inicia o jogo:
            # if state == HOME1:
            # #Rodar tela inicial
            #     screen = pygame.display.set_mode((WIDTH, HEIGHT))
            #     state = fog_water_start(screen)
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player.speedx -= SPEED_X
            
                elif event.key == pygame.K_RIGHT:
                    player.speedx += SPEED_X
                    
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.jump()

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player.speedx += SPEED_X
        
                elif event.key == pygame.K_RIGHT:
                    player.speedx -= SPEED_X
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()

        #Verifica se passou para a próxima fase:
        if player.fase == '2' and player.speedx == 0 and player.speedy == 0:
            state = HOME2
            player.alive = 'alive'
            player.speedy = 0 
            player.speedx = 0
            break
    
        #Verifica se colidiu em água:
        if player.alive == 'dead':
            pygame.mixer.music.load('assets/som/Game_over.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1) 
            restart = game_over(screen)
            if restart:
                #Reincia:
                player.rect.x = TILE_SIZE
                player.rect.bottom = 15 * TILE_SIZE
                player.alive = 'alive'
                pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
                pygame.mixer.music.set_volume (2.0)
                pygame.mixer.music.play (-1)
                player.speedx = 0
                player.speedy = 0
                state = HOME1
             
            else:
                state = DONE
                player.speedx = 0
                player.speedy = 0

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    
    return state

def fase2(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    # Cria um grupo somente com os sprites de bloco.
    # Sprites de block são aqueles que impedem o movimento do jogador
    blocks = pygame.sprite.Group()
    agua = pygame.sprite.Group()
    veneno = pygame.sprite.Group()
    portas = pygame.sprite.Group()
    

    # Cria Sprite do jogador
    player = Player_Fogo(assets[PLAYER_IMG_FOGO],assets[PLAYER_IMG_FOGO_RUN],assets[PLAYER_IMG_FOGO_RUN_ESQ], 12, 2, blocks,agua,veneno,portas)

    # Cria tiles de acordo com o mapa
    for row in range(len(MAP2)):
        for column in range(len(MAP2[row])):
            tile_type = MAP2[row][column]
            if tile_type == BLOCK or tile_type == AGUA or tile_type == FOGO or tile_type == VENENO or tile_type == PORTA_AGUA or tile_type == PORTA_FOGO:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                if tile_type != PORTA_FOGO and tile_type!= PORTA_AGUA:
                    blocks.add(tile)
                else:
                    portas.add(tile)
            if tile_type == AGUA:
                tile = Tile(assets[tile_type], row, column)
                agua.add(tile)
            if tile_type == VENENO:
                tile = Tile(assets[tile_type], row, column)
                veneno.add(tile)
    
    # Adiciona o jogador no grupo de sprites por último para ser desenhado por
    # cima dos blocos
    all_sprites.add(player)


    state = HOME2

    if player.alive != "dead":
            pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
            pygame.mixer.music.set_volume (2.0)
            pygame.mixer.music.play (-1)
    
    while state != DONE:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():

            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE

            # # Verifica se inicia o jogo:
            # if state == HOME2:
            # #Rodar tela inicial
            #     screen = pygame.display.set_mode((WIDTH, HEIGHT))
            #     state = fog_water_start(screen)
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player.speedx -= SPEED_X
            
                elif event.key == pygame.K_RIGHT:
                    player.speedx += SPEED_X
                    
                elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
                    player.jump()

            # Verifica se soltou alguma tecla.
            if event.type == pygame.KEYUP:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player.speedx += SPEED_X
        
                elif event.key == pygame.K_RIGHT:
                    player.speedx -= SPEED_X
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()
    
        #Verifica se colidiu em água:
        if player.alive == 'dead':
            pygame.mixer.music.load('assets/som/Game_over.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1) 
            restart = game_over(screen)
            if restart:
                #Reincia:
                player.rect.x = TILE_SIZE
                player.rect.bottom = 15 * TILE_SIZE
                player.alive = 'alive'
                pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
                pygame.mixer.music.set_volume (2.0)
                pygame.mixer.music.play (-1)
                player.speedx = 0
                player.speedy = 0
                state = HOME2
             
            else:
                state = DONE

    
        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    
    return state



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
