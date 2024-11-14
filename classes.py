import pygame
import random
from constantes import *


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


# Classe Jogador que representa o herói fogo:
class Player_Fogo(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, player_img_fogo,player_img_fogo_run,player_img_fogo_run_esq, row, column, blocks, agua,veneno,porta_fogo,blocos_inimigo_verde, fase):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.state = STILL
        self.alive = 'alive'
        self.fase = fase
        self.fase_atual = fase

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
        self.porta_fogo = porta_fogo
        self.blocos_inimigo_verde = blocos_inimigo_verde

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
        
        # Se colidiu com algum bloco de movimento VERDE, personagem morre:
        collisions = pygame.sprite.spritecollide(self, self.blocos_inimigo_verde, False)
        if len(collisions) != 0:
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
        collisions = pygame.sprite.spritecollide(self, self.porta_fogo, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            if self.rect.right < collision.rect.right + 10  and self.rect.left > collision.rect.left - 10: 
                self.rect.center = collision.rect.center
                self.fase = str(int(self.fase_atual)+1)
                

    # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING



# Classe Jogador que representa o herói fogo:
class Player_Agua(pygame.sprite.Sprite):

    # Construtor da classe.
    def __init__(self, player_img_agua,player_img_agua_run,player_img_agua_run_esq, row, column, blocks, fogo,veneno,porta_agua,blocos_inimigo_verde, fase):

        # Construtor da classe pai (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Define estado atual
        # Usamos o estado para decidir se o jogador pode ou não pular
        self.state = STILL
        self.alive = 'alive'
        self.fase = fase
        self.fase_atual = fase

        # Ajusta o tamanho da imagem
        self.player_img_agua = pygame.transform.scale(player_img_agua, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.player_img_agua_run = pygame.transform.scale(player_img_agua_run, (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.player_img_agua_run_esq = pygame.transform.scale(player_img_agua_run_esq, (PLAYER_WIDTH, PLAYER_HEIGHT))

        # Define a imagem do sprite. Imagem estática (não teremos animação durante o pulo):
        self.image = self.player_img_agua

        # Detalhes sobre o posicionamento.
        self.rect = self.image.get_rect()
        self.rect_run = self.image.get_rect()

        # Guarda o grupo de blocos para tratar as colisões
        self.blocks = blocks
        self.fogo = fogo
        self.veneno = veneno
        self.porta_agua = porta_agua
        self.blocos_inimigo_verde = blocos_inimigo_verde

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
        collisions = pygame.sprite.spritecollide(self, self.fogo, False)
        for collision in collisions:
            if self.rect.bottom < collision.rect.top + TILE_SIZE/2:
                self.alive = 'dead'
        
        # Se colidiu com algum bloco de VENENO, personagem morre:
        collisions = pygame.sprite.spritecollide(self, self.veneno, False)
        for collision in collisions:
            if self.rect.bottom < collision.rect.top + TILE_SIZE/2:
                self.alive = 'dead'
        
        # Se colidiu com algum bloco de movimento VERDE, personagem morre:
        collisions = pygame.sprite.spritecollide(self, self.blocos_inimigo_verde, False)
        if len(collisions) != 0:
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
            self.image = self.player_img_agua_run
        elif self.speedx < 0:
            self.image = self.player_img_agua_run_esq
        else:
            self.image = self.player_img_agua
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
        collisions = pygame.sprite.spritecollide(self, self.porta_agua, False)
        # Corrige a posição do personagem para antes da colisão
        for collision in collisions:
            if self.rect.right < collision.rect.right + 10  and self.rect.left > collision.rect.left - 10: 
                self.rect.center = collision.rect.center
                self.fase = str(int(self.fase_atual)+1)

    # Método que faz o personagem pular
    def jump(self):
        # Só pode pular se ainda não estiver pulando ou caindo
        if self.state == STILL:
            self.speedy -= JUMP_SIZE
            self.state = JUMPING


#Classe inimigo, movimento aleatório:
class Inimigo_Agua(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, largura, altura, velocidade):
        super().__init__()
        self.image = pygame.Surface((largura, altura))
        self.image.fill((0, 135, 0))  # Define a cor do inimigo (vermelho)
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))
        self.velocidade = velocidade
        self.direcao = random.choice([-1, 1])  # Define a direção inicial (esquerda ou direita)
        self.limite_esquerdo = pos_x - 2*largura
        self.limite_direito = pos_x + 2*largura

    def update(self):
        self.rect.x += self.velocidade * self.direcao
        if self.rect.left <= self.limite_esquerdo or self.rect.right >= self.limite_direito:
            self.direcao *= -1