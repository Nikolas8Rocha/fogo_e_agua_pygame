import pygame
import time
from constantes import *
from classes import *
from utils import *

def fase1(screen, score_agua, score_fogo):
# Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)

    # Crie o Scoreboard
    scoreboard= Scoreboard(WIDTH/2, 10)

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    # Cria um grupo somente com os sprites de bloco.
    # Sprites de block são aqueles que impedem o movimento do jogador
    blocks = pygame.sprite.Group()
    fogo = pygame.sprite.Group()
    agua = pygame.sprite.Group()
    veneno = pygame.sprite.Group()
    porta_fogo = pygame.sprite.Group()
    porta_agua = pygame.sprite.Group()
    blocos_inimigo_verde = pygame.sprite.Group()
    diamante_agua = pygame.sprite.Group()
    diamante_fogo = pygame.sprite.Group()
    
    #Cria Sprite do inimigo:
    inimigo_agua_1 = Inimigo_Agua(530,330,15,15,1)
    blocos_inimigo_verde.add(inimigo_agua_1)
    inimigo_agua_2 = Inimigo_Agua(660,170,15,15,1)
    blocos_inimigo_verde.add(inimigo_agua_2)
    
    diamante_agua_1 = Diamante_Agua(50,170,DIAMANTE_A)
    diamante_agua_2 = Diamante_Agua(50,495,DIAMANTE_A)
    diamante_agua_3 = Diamante_Agua(452, 215, DIAMANTE_A)

    diamante_fogo_1 = Diamante_Fogo(90, 55, DIAMANTE_F)
    diamante_fogo_2 = Diamante_Fogo(100, 495, DIAMANTE_F)
    diamante_fogo_3 = Diamante_Fogo(357, 370, DIAMANTE_F)
    
    
    diamante_agua.add(diamante_agua_1)
    diamante_agua.add(diamante_agua_2)
    diamante_agua.add(diamante_agua_3)

    diamante_fogo.add(diamante_fogo_1)
    diamante_fogo.add(diamante_fogo_2)
    diamante_fogo.add(diamante_fogo_3)


    # Cria Sprite do jogador
    player_fogo = Player_Fogo(assets[PLAYER_IMG_FOGO],assets[PLAYER_IMG_FOGO_RUN],assets[PLAYER_IMG_FOGO_RUN_ESQ], 12, 2, blocks,agua,veneno,porta_fogo,blocos_inimigo_verde,diamante_fogo,score_fogo, '1')
    player_agua = Player_Agua(assets[PLAYER_IMG_AGUA],assets[PLAYER_IMG_AGUA_RUN],assets[PLAYER_IMG_AGUA_RUN_ESQ], 12, 2, blocks,fogo,veneno,porta_agua,blocos_inimigo_verde,diamante_agua,score_agua, '1')

    # Cria tiles de acordo com o mapa
    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            if tile_type == BLOCK or tile_type == AGUA or tile_type == FOGO or tile_type == VENENO or tile_type == PORTA_AGUA or tile_type == PORTA_FOGO:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                if tile_type != PORTA_FOGO and tile_type!= PORTA_AGUA:
                    blocks.add(tile)
                elif tile_type == PORTA_FOGO:
                    porta_fogo.add(tile)
                elif tile_type == PORTA_AGUA:
                    porta_agua.add(tile)
            if tile_type == AGUA:
                tile = Tile(assets[tile_type], row, column)
                agua.add(tile)
            if tile_type == VENENO:
                tile = Tile(assets[tile_type], row, column)
                veneno.add(tile)
            if tile_type == FOGO:
                tile = Tile(assets[tile_type], row, column)
                fogo.add(tile)
    
    # Adiciona o jogador no grupo de sprites por último para ser desenhado por
    # cima dos blocos
    all_sprites.add(player_fogo)
    all_sprites.add(player_agua)
    all_sprites.add(inimigo_agua_1)
    all_sprites.add(inimigo_agua_2)
    all_sprites.add(diamante_agua_1)
    all_sprites.add(diamante_agua_2)
    all_sprites.add(diamante_agua_3)

    all_sprites.add(diamante_fogo_1)
    all_sprites.add(diamante_fogo_2)
    all_sprites.add(diamante_fogo_3)


    state = HOME1

    if player_fogo.alive != "dead" and player_agua.alive != 'dead':
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

            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador fogo:
                if event.key == pygame.K_LEFT:
                    player_fogo.speedx -= SPEED_X
            
                elif event.key == pygame.K_RIGHT:
                    player_fogo.speedx += SPEED_X
                    
                elif event.key == pygame.K_UP:
                    player_fogo.jump()
                
                # Dependendo da tecla, altera o estado do jogador agua:
                if event.key == pygame.K_a:
                    player_agua.speedx -= SPEED_X
            
                elif event.key == pygame.K_d:
                    player_agua.speedx += SPEED_X
                    
                elif event.key == pygame.K_w:
                    player_agua.jump()

            # Verifica se soltou alguma tecla -- jogoador fogo:
            if event.type == pygame.KEYUP and player_fogo.speedx != 0:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player_fogo.speedx += SPEED_X
        
                elif event.key == pygame.K_RIGHT:
                    player_fogo.speedx -= SPEED_X
            
            # Verifica se soltou alguma tecla -- jogoador agua:
            if event.type == pygame.KEYUP and player_agua.speedx != 0:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_a:
                    player_agua.speedx += SPEED_X
        
                elif event.key == pygame.K_d:
                    player_agua.speedx -= SPEED_X
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()

        #Verifica se passou para a próxima fase:
        if player_fogo.fase == '2' and player_agua.fase == '2' and  player_fogo.speedx == 0 and player_fogo.speedy == 0:
            state = HOME2
            player_fogo.alive = 'alive'
            player_fogo.speedy = 0 
            player_fogo.speedx = 0
            time.sleep(0.2)
            break
    
        #Verifica se o player_fogo colidiu em água ou veneno:
        if player_fogo.alive == 'dead':
            pygame.mixer.music.load('assets/som/Game_over.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1) 
            restart = game_over(screen)
            if restart:
                #Reincia PLAYER_FOGO:
                player_fogo.rect.x = TILE_SIZE
                player_fogo.rect.bottom = 15 * TILE_SIZE
                player_fogo.alive = 'alive'
                pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
                pygame.mixer.music.set_volume (2.0)
                pygame.mixer.music.play (-1)
                player_fogo.speedx = 0
                player_fogo.speedy = 0
                state = HOME1

                #Reincia PLAYER_AGUA:
                player_agua.rect.x = TILE_SIZE
                player_agua.rect.bottom = 15 * TILE_SIZE
                player_agua.alive = 'alive'
                pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
                pygame.mixer.music.set_volume (2.0)
                pygame.mixer.music.play (-1)
                player_agua.speedx = 0
                player_agua.speedy = 0
                state = HOME1
             
            else:
                state = DONE
                player_fogo.speedx = 0
                player_fogo.speedy = 0

        #Verifica se o player_agua colidiu em fogo ou veneno:
        if player_agua.alive == 'dead':
            pygame.mixer.music.load('assets/som/Game_over.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1) 
            restart = game_over(screen)
            if restart:
                #Reincia PLAYER_FOGO:
                player_fogo.rect.x = TILE_SIZE
                player_fogo.rect.bottom = 15 * TILE_SIZE
                player_fogo.alive = 'alive'
                pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
                pygame.mixer.music.set_volume (2.0)
                pygame.mixer.music.play (-1)
                player_fogo.speedx = 0
                player_fogo.speedy = 0
                state = HOME1

                #Reincia PLAYER_AGUA:
                player_agua.rect.x = TILE_SIZE
                player_agua.rect.bottom = 15 * TILE_SIZE
                player_agua.alive = 'alive'
                pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
                pygame.mixer.music.set_volume (2.0)
                pygame.mixer.music.play (-1)
                player_agua.speedx = 0
                player_agua.speedy = 0
                state = HOME1
             
            else:
                state = DONE
                player_agua.speedx = 0
                player_agua.speedy = 0

        # Atualize a pontuação
        scoreboard.set_score(player_agua.score_agua, player_fogo.score_fogo)
        scoreboard.update_score(0, 0)

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Desenha o Scoreboard
        scoreboard.draw(screen)  # Desenha o Scoreboard geral

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    
    return state, [player_agua.score_agua, player_fogo.score_fogo]

def fase2(screen, score_agua, score_fogo):
# Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)

    # Crie o Scoreboard
    scoreboard= Scoreboard(WIDTH/2, 10)

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    # Cria um grupo somente com os sprites de bloco.
    # Sprites de block são aqueles que impedem o movimento do jogador
    blocks = pygame.sprite.Group()
    fogo = pygame.sprite.Group()
    agua = pygame.sprite.Group()
    veneno = pygame.sprite.Group()
    porta_fogo = pygame.sprite.Group()
    porta_agua = pygame.sprite.Group()
    blocos_inimigo_verde = pygame.sprite.Group()
    diamante_agua = pygame.sprite.Group()
    diamante_fogo = pygame.sprite.Group()
    
    #Cria Sprite do inimigo:
    inimigo_agua_1 = Inimigo_Agua(455,320,15,15,1)
    blocos_inimigo_verde.add(inimigo_agua_1)
    inimigo_agua_2 = Inimigo_Agua(480,120,15,15,1)
    blocos_inimigo_verde.add(inimigo_agua_2)
    inimigo_agua_3 = Inimigo_Agua(330,550,25,25,1)
    blocos_inimigo_verde.add(inimigo_agua_3)
    inimigo_agua_4 = Inimigo_Agua(580,550,25,25,1)
    blocos_inimigo_verde.add(inimigo_agua_4)

    diamante_agua_1 = Diamante_Agua(50,210,DIAMANTE_A)
    diamante_agua_2 = Diamante_Agua(970,50,DIAMANTE_A)
    diamante_agua_3 = Diamante_Agua(850, 570, DIAMANTE_A)

    diamante_fogo_1 = Diamante_Fogo(55, 50, DIAMANTE_F)
    diamante_fogo_2 = Diamante_Fogo(970, 250, DIAMANTE_F)
    diamante_fogo_3 = Diamante_Fogo(900, 570, DIAMANTE_F)

    diamante_agua.add(diamante_agua_1)
    diamante_agua.add(diamante_agua_2)
    diamante_agua.add(diamante_agua_3)

    diamante_fogo.add(diamante_fogo_1)
    diamante_fogo.add(diamante_fogo_2)
    diamante_fogo.add(diamante_fogo_3)


    # Cria Sprite do jogador
    player_agua = Player_Agua(assets[PLAYER_IMG_AGUA],assets[PLAYER_IMG_AGUA_RUN],assets[PLAYER_IMG_AGUA_RUN_ESQ], 12, 2, blocks,fogo,veneno,porta_agua,blocos_inimigo_verde,diamante_agua,score_agua, '2')
    player_fogo = Player_Fogo(assets[PLAYER_IMG_FOGO],assets[PLAYER_IMG_FOGO_RUN],assets[PLAYER_IMG_FOGO_RUN_ESQ], 12, 2, blocks,agua,veneno,porta_fogo,blocos_inimigo_verde,diamante_fogo,score_fogo, '2')
    # Cria tiles de acordo com o mapa
    for row in range(len(MAP2)):
        for column in range(len(MAP2[row])):
            tile_type = MAP2[row][column]
            if tile_type == BLOCK or tile_type == AGUA or tile_type == FOGO or tile_type == VENENO or tile_type == PORTA_AGUA or tile_type == PORTA_FOGO:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                if tile_type != PORTA_FOGO and tile_type!= PORTA_AGUA:
                    blocks.add(tile)
                elif tile_type == PORTA_FOGO:
                    porta_fogo.add(tile)
                elif tile_type == PORTA_AGUA:
                    porta_agua.add(tile)
            if tile_type == AGUA:
                tile = Tile(assets[tile_type], row, column)
                agua.add(tile)
            if tile_type == VENENO:
                tile = Tile(assets[tile_type], row, column)
                veneno.add(tile)
            if tile_type == FOGO:
                tile = Tile(assets[tile_type], row, column)
                fogo.add(tile)
    
    # Adiciona o jogador no grupo de sprites por último para ser desenhado por
    # cima dos blocos
    all_sprites.add(player_fogo)
    all_sprites.add(player_agua)
    all_sprites.add(inimigo_agua_1)
    all_sprites.add(inimigo_agua_2)
    all_sprites.add(inimigo_agua_3)
    all_sprites.add(inimigo_agua_4)

    all_sprites.add(diamante_agua_1)
    all_sprites.add(diamante_agua_2)
    all_sprites.add(diamante_agua_3)

    all_sprites.add(diamante_fogo_1)
    all_sprites.add(diamante_fogo_2)
    all_sprites.add(diamante_fogo_3)

    state = HOME2

    if player_fogo.alive != "dead" and player_agua.alive != 'dead':
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

            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador fogo:
                if event.key == pygame.K_LEFT:
                    player_fogo.speedx -= SPEED_X
            
                elif event.key == pygame.K_RIGHT:
                    player_fogo.speedx += SPEED_X
                    
                elif event.key == pygame.K_UP:
                    player_fogo.jump()
                
                # Dependendo da tecla, altera o estado do jogador agua:
                if event.key == pygame.K_a:
                    player_agua.speedx -= SPEED_X
            
                elif event.key == pygame.K_d:
                    player_agua.speedx += SPEED_X
                    
                elif event.key == pygame.K_w:
                    player_agua.jump()

            # Verifica se soltou alguma tecla -- jogoador fogo:
            if event.type == pygame.KEYUP and player_fogo.speedx != 0:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player_fogo.speedx += SPEED_X
        
                elif event.key == pygame.K_RIGHT:
                    player_fogo.speedx -= SPEED_X
            
            # Verifica se soltou alguma tecla -- jogoador agua:
            if event.type == pygame.KEYUP and player_agua.speedx != 0:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_a:
                    player_agua.speedx += SPEED_X
        
                elif event.key == pygame.K_d:
                    player_agua.speedx -= SPEED_X
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()

        #Verifica se passou para a próxima fase:
        if player_fogo.fase == '3' and player_agua.fase == '3' and  player_fogo.speedx == 0 and player_fogo.speedy == 0:
            state = HOME3
            player_fogo.alive = 'alive'
            player_fogo.speedy = 0 
            player_fogo.speedx = 0
            time.sleep(0.2)
            break
    
        #Verifica se o player_fogo colidiu em água ou veneno:
        if player_fogo.alive == 'dead':
            pygame.mixer.music.load('assets/som/Game_over.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1) 
            restart = game_over(screen)
            if restart:
                #Reincia PLAYER_FOGO:
                player_fogo.rect.x = TILE_SIZE
                player_fogo.rect.bottom = 15 * TILE_SIZE
                player_fogo.alive = 'alive'
                pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
                pygame.mixer.music.set_volume (2.0)
                pygame.mixer.music.play (-1)
                player_fogo.speedx = 0
                player_fogo.speedy = 0
                state = HOME1

                #Reincia PLAYER_AGUA:
                player_agua.rect.x = TILE_SIZE
                player_agua.rect.bottom = 15 * TILE_SIZE
                player_agua.alive = 'alive'
                pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
                pygame.mixer.music.set_volume (2.0)
                pygame.mixer.music.play (-1)
                player_agua.speedx = 0
                player_agua.speedy = 0
                state = HOME1
             
            else:
                state = DONE
                player_fogo.speedx = 0
                player_fogo.speedy = 0

        #Verifica se o player_agua colidiu em fogo ou veneno:
        if player_agua.alive == 'dead':
            pygame.mixer.music.load('assets/som/Game_over.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1) 
            restart = game_over(screen)
            if restart:
                #Reincia PLAYER_FOGO:
                player_fogo.rect.x = TILE_SIZE
                player_fogo.rect.bottom = 15 * TILE_SIZE
                player_fogo.alive = 'alive'
                pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
                pygame.mixer.music.set_volume (2.0)
                pygame.mixer.music.play (-1)
                player_fogo.speedx = 0
                player_fogo.speedy = 0
                state = HOME1

                #Reincia PLAYER_AGUA:
                player_agua.rect.x = TILE_SIZE
                player_agua.rect.bottom = 15 * TILE_SIZE
                player_agua.alive = 'alive'
                player_agua.speedx = 0
                player_agua.speedy = 0
                state = HOME1
             
            else:
                state = DONE
                player_agua.speedx = 0
                player_agua.speedy = 0

        # Atualize a pontuação
        scoreboard.set_score(player_agua.score_agua, player_fogo.score_fogo)
        scoreboard.update_score(0, 0)

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Desenha o Scoreboard
        scoreboard.draw(screen)  # Desenha o Scoreboard geral

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    
    return state, [player_agua.score_agua, player_fogo.score_fogo]

def fase3(screen, score_agua, score_fogo):
# Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)

    # Crie o Scoreboard
    scoreboard= Scoreboard(WIDTH/2, 10)

    # Cria um grupo de todos os sprites.
    all_sprites = pygame.sprite.Group()
    # Cria um grupo somente com os sprites de bloco.
    # Sprites de block são aqueles que impedem o movimento do jogador
    blocks = pygame.sprite.Group()
    fogo = pygame.sprite.Group()
    agua = pygame.sprite.Group()
    veneno = pygame.sprite.Group()
    porta_fogo = pygame.sprite.Group()
    porta_agua = pygame.sprite.Group()
    blocos_inimigo_verde = pygame.sprite.Group()

    diamante_agua = pygame.sprite.Group()
    diamante_fogo = pygame.sprite.Group()
    
    #Cria Sprite do inimigo:
    inimigo_agua_1 = Inimigo_Agua(105,200,15,15,1)
    blocos_inimigo_verde.add(inimigo_agua_1)
    inimigo_agua_2 = Inimigo_Agua(500,300,15,15,1)
    blocos_inimigo_verde.add(inimigo_agua_2)
    inimigo_agua_3 = Inimigo_Agua(105,500,15,15,1)
    blocos_inimigo_verde.add(inimigo_agua_3)
    inimigo_agua_4 = Inimigo_Agua(250,175,15,15,1)
    blocos_inimigo_verde.add(inimigo_agua_4)
    
    inimigo_agua_5 = Inimigo_Agua(660,185,15,15,1)
    blocos_inimigo_verde.add(inimigo_agua_5)
    inimigo_agua_6 = Inimigo_Agua(800,115,15,15,1) #DO CANTO
    blocos_inimigo_verde.add(inimigo_agua_6)
    inimigo_agua_7 = Inimigo_Agua(560,485,15,15,1)
    blocos_inimigo_verde.add(inimigo_agua_7)

    diamante_agua_1 = Diamante_Agua(340,95,DIAMANTE_A)
    diamante_agua_2 = Diamante_Agua(1010,70,DIAMANTE_A)
    diamante_agua_3 = Diamante_Agua(330, 540, DIAMANTE_A)

    diamante_fogo_1 = Diamante_Fogo(380, 95, DIAMANTE_F)
    diamante_fogo_2 = Diamante_Fogo(1010, 95, DIAMANTE_F)
    diamante_fogo_3 = Diamante_Fogo(330, 570, DIAMANTE_F)

    diamante_agua.add(diamante_agua_1)
    diamante_agua.add(diamante_agua_2)
    diamante_agua.add(diamante_agua_3)

    diamante_fogo.add(diamante_fogo_1)
    diamante_fogo.add(diamante_fogo_2)
    diamante_fogo.add(diamante_fogo_3)


    # Cria Sprite do jogador
    player_fogo = Player_Fogo(assets[PLAYER_IMG_FOGO],assets[PLAYER_IMG_FOGO_RUN],assets[PLAYER_IMG_FOGO_RUN_ESQ], 12, 2, blocks,agua,veneno,porta_fogo,blocos_inimigo_verde,diamante_fogo,score_fogo, '3')
    player_agua = Player_Agua(assets[PLAYER_IMG_AGUA],assets[PLAYER_IMG_AGUA_RUN],assets[PLAYER_IMG_AGUA_RUN_ESQ], 12, 2, blocks,fogo,veneno,porta_agua,blocos_inimigo_verde,diamante_agua,score_agua, '3')
    # Cria tiles de acordo com o mapa
    for row in range(len(MAP3)):
        for column in range(len(MAP3[row])):
            tile_type = MAP3[row][column]
            if tile_type == BLOCK or tile_type == AGUA or tile_type == FOGO or tile_type == VENENO or tile_type == PORTA_AGUA or tile_type == PORTA_FOGO:
                tile = Tile(assets[tile_type], row, column)
                all_sprites.add(tile)
                if tile_type != PORTA_FOGO and tile_type!= PORTA_AGUA:
                    blocks.add(tile)
                elif tile_type == PORTA_FOGO:
                    porta_fogo.add(tile)
                elif tile_type == PORTA_AGUA:
                    porta_agua.add(tile)
            if tile_type == AGUA:
                tile = Tile(assets[tile_type], row, column)
                agua.add(tile)
            if tile_type == VENENO:
                tile = Tile(assets[tile_type], row, column)
                veneno.add(tile)
            if tile_type == FOGO:
                tile = Tile(assets[tile_type], row, column)
                fogo.add(tile)
    
    # Adiciona o jogador no grupo de sprites por último para ser desenhado por
    # cima dos blocos
    all_sprites.add(player_fogo)
    all_sprites.add(player_agua)
    all_sprites.add(inimigo_agua_1)
    all_sprites.add(inimigo_agua_2)
    all_sprites.add(inimigo_agua_3)
    all_sprites.add(inimigo_agua_4)
    all_sprites.add(inimigo_agua_5)
    all_sprites.add(inimigo_agua_6)
    all_sprites.add(inimigo_agua_7)

    all_sprites.add(diamante_agua_1)
    all_sprites.add(diamante_agua_2)
    all_sprites.add(diamante_agua_3)
    
    all_sprites.add(diamante_fogo_1)
    all_sprites.add(diamante_fogo_2)
    all_sprites.add(diamante_fogo_3)


    state = HOME3

    if player_fogo.alive != "dead" and player_agua.alive != 'dead':
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

            if event.type == pygame.KEYDOWN:
                # Dependendo da tecla, altera o estado do jogador fogo:
                if event.key == pygame.K_LEFT:
                    player_fogo.speedx -= SPEED_X
            
                elif event.key == pygame.K_RIGHT:
                    player_fogo.speedx += SPEED_X
                    
                elif event.key == pygame.K_UP:
                    player_fogo.jump()
                
                # Dependendo da tecla, altera o estado do jogador agua:
                if event.key == pygame.K_a:
                    player_agua.speedx -= SPEED_X
            
                elif event.key == pygame.K_d:
                    player_agua.speedx += SPEED_X
                    
                elif event.key == pygame.K_w:
                    player_agua.jump()

            # Verifica se soltou alguma tecla -- jogoador fogo:
            if event.type == pygame.KEYUP and player_fogo.speedx != 0:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_LEFT:
                    player_fogo.speedx += SPEED_X
        
                elif event.key == pygame.K_RIGHT:
                    player_fogo.speedx -= SPEED_X
            
            # Verifica se soltou alguma tecla -- jogoador agua:
            if event.type == pygame.KEYUP and player_agua.speedx != 0:
                # Dependendo da tecla, altera o estado do jogador.
                if event.key == pygame.K_a:
                    player_agua.speedx += SPEED_X
        
                elif event.key == pygame.K_d:
                    player_agua.speedx -= SPEED_X
                    
        # Depois de processar os eventos.
        # Atualiza a acao de cada sprite. O grupo chama o método update() de cada Sprite dentre dele.
        all_sprites.update()

        #Verifica se passou para a próxima fase:
        if player_fogo.fase == '4' and player_agua.fase == '4' and  player_fogo.speedx == 0 and player_fogo.speedy == 0:
            time.sleep(0.5)
            if vitoria(screen):
                state = INIT
                player_fogo.alive = 'alive'
                player_fogo.speedy = 0 
                player_fogo.speedx = 0
                break
            
            else:
                state = DONE
                player_fogo.speedx = 0
                player_fogo.speedy = 0
    
        #Verifica se o player_fogo colidiu em água ou veneno:
        if player_fogo.alive == 'dead':
            pygame.mixer.music.load('assets/som/Game_over.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1) 
            restart = game_over(screen)
            if restart:
                #Reincia PLAYER_FOGO:
                player_fogo.rect.x = TILE_SIZE
                player_fogo.rect.bottom = 15 * TILE_SIZE
                player_fogo.alive = 'alive'
                pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
                pygame.mixer.music.set_volume (2.0)
                pygame.mixer.music.play (-1)
                player_fogo.speedx = 0
                player_fogo.speedy = 0
                state = HOME3

                #Reincia PLAYER_AGUA:
                player_agua.rect.x = TILE_SIZE
                player_agua.rect.bottom = 15 * TILE_SIZE
                player_agua.alive = 'alive'
                pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
                pygame.mixer.music.set_volume (2.0)
                pygame.mixer.music.play (-1)
                player_agua.speedx = 0
                player_agua.speedy = 0
                state = HOME3
             
            else:
                state = DONE
                player_fogo.speedx = 0
                player_fogo.speedy = 0

        #Verifica se o player_agua colidiu em fogo ou veneno:
        if player_agua.alive == 'dead':
            pygame.mixer.music.load('assets/som/Game_over.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1) 
            restart = game_over(screen)
            if restart:
                #Reincia PLAYER_FOGO:
                player_fogo.rect.x = TILE_SIZE
                player_fogo.rect.bottom = 15 * TILE_SIZE
                player_fogo.alive = 'alive'
                pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
                pygame.mixer.music.set_volume (2.0)
                pygame.mixer.music.play (-1)
                player_fogo.speedx = 0
                player_fogo.speedy = 0
                state = HOME3

                #Reincia PLAYER_AGUA:
                player_agua.rect.x = TILE_SIZE
                player_agua.rect.bottom = 15 * TILE_SIZE
                player_agua.alive = 'alive'
                pygame.mixer.music.load('assets/som/Menu_inicial.mp3')
                pygame.mixer.music.set_volume (2.0)
                pygame.mixer.music.play (-1)
                player_agua.speedx = 0
                player_agua.speedy = 0
                state = HOME3
             
            else:
                state = DONE
                player_agua.speedx = 0
                player_agua.speedy = 0

        # Atualize a pontuação
        scoreboard.set_score(player_agua.score_agua, player_fogo.score_fogo)
        scoreboard.update_score(0, 0)

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Desenha o Scoreboard
        scoreboard.draw(screen)  # Desenha o Scoreboard geral

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    return state, [player_agua.score_agua, player_fogo.score_fogo]