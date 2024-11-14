import pygame
import time
from constantes import *
from classes import *
from utils import *

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
    fogo = pygame.sprite.Group()
    agua = pygame.sprite.Group()
    veneno = pygame.sprite.Group()
    porta_fogo = pygame.sprite.Group()
    porta_agua = pygame.sprite.Group()
    blocos_inimigo_verde = pygame.sprite.Group()
    diamante_agua = pygame.sprite.Group()
    diamante_fogo = pygame.sprite.Group()
    
    #Cria Sprite do inimigo:
    inimigo_agua_1 = Inimigo_Agua(530,320,15,15,1)
    blocos_inimigo_verde.add(inimigo_agua_1)
    inimigo_agua_2 = Inimigo_Agua(660,170,15,15,1)
    blocos_inimigo_verde.add(inimigo_agua_2)
    diamante_agua_1 = Diamante_Agua(500,100,)
    diamante_agua_2 = Diamante_Agua(400,100,)
    diamante_agua.add(diamante_agua_1)
    diamante_agua.add(diamante_agua_2)


    # Cria Sprite do jogador
    player_fogo = Player_Fogo(assets[PLAYER_IMG_FOGO],assets[PLAYER_IMG_FOGO_RUN],assets[PLAYER_IMG_FOGO_RUN_ESQ], 12, 2, blocks,agua,veneno,porta_fogo,blocos_inimigo_verde,diamante_agua, '1')
    player_agua = Player_Agua(assets[PLAYER_IMG_AGUA],assets[PLAYER_IMG_AGUA_RUN],assets[PLAYER_IMG_AGUA_RUN_ESQ], 12, 2, blocks,fogo,veneno,porta_agua,blocos_inimigo_verde,diamante_fogo, '1')

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
    fogo = pygame.sprite.Group()
    agua = pygame.sprite.Group()
    veneno = pygame.sprite.Group()
    porta_fogo = pygame.sprite.Group()
    porta_agua = pygame.sprite.Group()
    blocos_inimigo_verde = pygame.sprite.Group()
    
    #Cria Sprite do inimigo:
    inimigo_agua_1 = Inimigo_Agua(530,320,15,15,1)
    blocos_inimigo_verde.add(inimigo_agua_1)
    inimigo_agua_2 = Inimigo_Agua(660,170,15,15,1)
    blocos_inimigo_verde.add(inimigo_agua_2)


    # Cria Sprite do jogador
    player_fogo = Player_Fogo(assets[PLAYER_IMG_FOGO],assets[PLAYER_IMG_FOGO_RUN],assets[PLAYER_IMG_FOGO_RUN_ESQ], 12, 2, blocks,agua,veneno,porta_fogo,blocos_inimigo_verde, '2')
    player_agua = Player_Agua(assets[PLAYER_IMG_AGUA],assets[PLAYER_IMG_AGUA_RUN],assets[PLAYER_IMG_AGUA_RUN_ESQ], 12, 2, blocks,fogo,veneno,porta_agua,blocos_inimigo_verde, '2')

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

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    
    return state

def fase3(screen):
# Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega assets
    assets = load_assets(img_dir)

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
    
    #Cria Sprite do inimigo:
    inimigo_agua_1 = Inimigo_Agua(530,320,15,15,1)
    blocos_inimigo_verde.add(inimigo_agua_1)
    inimigo_agua_2 = Inimigo_Agua(660,170,15,15,1)
    blocos_inimigo_verde.add(inimigo_agua_2)


    # Cria Sprite do jogador
    player_fogo = Player_Fogo(assets[PLAYER_IMG_FOGO],assets[PLAYER_IMG_FOGO_RUN],assets[PLAYER_IMG_FOGO_RUN_ESQ], 12, 2, blocks,agua,veneno,porta_fogo,blocos_inimigo_verde, '3')
    player_agua = Player_Agua(assets[PLAYER_IMG_AGUA],assets[PLAYER_IMG_AGUA_RUN],assets[PLAYER_IMG_AGUA_RUN_ESQ], 12, 2, blocks,fogo,veneno,porta_agua,blocos_inimigo_verde, '3')

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

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)
        all_sprites.draw(screen)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
    
    return state