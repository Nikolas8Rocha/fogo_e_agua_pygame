# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()
WIDTH = 1400 #largura da tela
HEIGHT = 700 #altura da tela
# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo do Pedro')

# ----- Inicia estruturas de dados
game = True
background_inicial = pygame.image.load("assets/img/tela_fundo_inicial.png").convert()
background_inicial = pygame.transform.scale(background_inicial,(WIDTH,HEIGHT))
# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.KEYUP:
            game = False
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background_inicial,(0,0))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
