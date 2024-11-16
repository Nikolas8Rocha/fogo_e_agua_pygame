import pygame
import random
from os import path
from constantes import *

# # Estabelece a pasta que contem as figuras e sons.
img_dir = path.join(path.dirname(__file__), 'assets/img')

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
    def __init__(self, player_img_fogo,player_img_fogo_run,player_img_fogo_run_esq, row, column, blocks, agua,veneno,porta_fogo,blocos_inimigo_verde,diamanate_fogo, score_fogo, fase):

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
        self.diamanate_fogo = diamanate_fogo

        # Posiciona o personagem
        # row é o índice da linha embaixo do personagem
        self.rect.x = TILE_SIZE
        self.rect.bottom = HEIGHT - TILE_SIZE

        self.speedx = 0
        self.speedy = 0
        self.score_fogo = score_fogo
        

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

        #Verifica se colidiu com o diamante:
        collisions = pygame.sprite.spritecollide(self, self.diamanate_fogo, True)
        if len(collisions) != 0:
            self.score_fogo += 100

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
    def __init__(self, player_img_agua,player_img_agua_run,player_img_agua_run_esq, row, column, blocks, fogo,veneno,porta_agua,blocos_inimigo_verde,diamante_agua,score_agua, fase):

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
        self.diamante_agua = diamante_agua

        # Posiciona o personagem
        # row é o índice da linha embaixo do personagem
        self.rect.x = TILE_SIZE
        self.rect.bottom = HEIGHT - TILE_SIZE

        self.speedx = 0
        self.speedy = 0
        self.score_agua = score_agua
        

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

        #Verifica se colidiu com o diamante_agua:
        collisions = pygame.sprite.spritecollide(self, self.diamante_agua, True)
        if len(collisions) != 0:
            self.score_agua += 100

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

#Classe diamante_agua:
class Diamante_Agua(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, imagem):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(imagem),(20,20)).convert_alpha()
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))

#Classe diamante_fogo:
class Diamante_Fogo(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, imagem):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(imagem),(20,20)).convert_alpha()
        self.rect = self.image.get_rect(topleft=(pos_x, pos_y))
    
# class Scoreboard:
#     def __init__(self, x, y, font_size=30):
#         self.score = 0  # Inicializa o score com 0
#         self.font = pygame.font.Font(None, font_size)
#         self.position = (x, y)

#     # Método para definir o score total (soma dos scores dos jogadores)
#     def set_score(self, score_agua, score_fogo):  
#         self.score = score_agua + score_fogo

#     # Método para atualizar o score (adiciona os scores dos jogadores)
#     def update_score(self, score_agua, score_fogo):
#         self.score += score_agua + score_fogo

#     def draw(self, surface):
#         score_surface = self.font.render(f'Diamantes: {self.score}', True, (255, 255, 255))
#         surface.blit(score_surface, self.position)

class Scoreboard:
    def __init__(self, x, y, font_size=30, imagem_path="estrela_score.png"):
        self.score = 0  # Inicializa o score com 0
        self.font = pygame.font.Font(None, font_size)
        self.position = (x, y)
        
        # Carrega a imagem do diamante
        self.imagem_diamante = pygame.image.load(imagem_path)
        
        # Redimensiona a imagem do diamante para as dimensões desejadas
        TILE_SIZE = 30  # Ajuste o valor conforme necessário
        self.imagem_diamante = pygame.transform.scale(self.imagem_diamante, (TILE_SIZE, TILE_SIZE))
        
        # Obtém o retângulo da imagem do diamante e define sua posição inicial
        self.retangulo_diamante = self.imagem_diamante.get_rect()
        self.retangulo_diamante.center = self.position

    def set_score(self, score_agua, score_fogo):
        self.score = score_agua + score_fogo         #Define o score como a soma de dois valores

    def update_score(self, score_agua, score_fogo):
        self.score += score_agua + score_fogo         #Atualiza o score somando os valores fornecidos

    def draw(self, surface):
        # Desenha a imagem do diamante
        surface.blit(self.imagem_diamante, self.retangulo_diamante)

        # Renderiza o score como texto
        score_surface = self.font.render(f'{self.score}', True, (255, 255, 255))
        score_rect = score_surface.get_rect()

        # Ajusta a posição do texto para centralizar verticalmente em relação à imagem do diamante
        texto_position = (
            self.position[0] + self.retangulo_diamante.width  ,  # Espaçamento horizontal
            self.position[1] - (score_rect.height // 3) + (self.retangulo_diamante.height // 100)  # Centralização vertical
        )
        
        # Desenha o texto na posição calculada
        surface.blit(score_surface, texto_position)