# fogo_e_agua_pygame
Jogo fogo e água

Nosso jogo se inspira, "fireboy and watergirl" (https://www.friv.com/z/games/fireboyandwatergirlforest/game.html). Nesse aspecto, vamos explicar como é a jogabilidade do nosso jogo a seguir:

- O jogo é feito para ser jogado em dupla, com um jogador movimentado o fireboy e outro a watergirl.
- O movimento dos jogadores é divido em: setas - fireboy e (w,a,s,d) -  watergirl
- O objetivo de cada fase é os dois jogadores chegarem nas portas, a partir do mombento que isso ocorre, o jogo muda de fase automáticamente.
- Existem dois tipos de diamantes no jogo, um tipo que somente o fireboy consegue pegar e outros que a watergirl pode pegar. Ao pegar os diamantes, a pontuação dos dois jogadores aumenta.

Esse jogo possui alguns desafios que devem ser superados, conforme as fases vão passando, há um aumento desses desafios. A seguir, detalharemos mais específicamente os desafios:
- blocos de fogo, os quais a watergirl não pode encostar.
- blocos de água, os quais o fireboy não pode encostar.
- blocos fixos de veneno, os quais nem a watergirl quanto o fireboy não podem encostarem.
- blocos de veneno móveis, os quais nem a watergirl quanto o fireboy não podem encostarem.
Se algum player encostar nesses blocos, ocorre o game over, e os jogadores voltam para as posições inicias, contudo nesse caso os diamantes não são resetados, ou seja, o que os player pegaram de diamantes antes de morres, não aprarecem mais na tela. 

Ao passar das três fases disponíveis no jogo, há a tela de vitória do jogo, com as seguintes condições:
- Pegam todos os diamantes do jogo (18): três estrelas 
- Pegam metade dos diamantes (9): duas estrelas
- Pegam menos da metade dos diamantes: uma estrela
- Não pegam nenhum diamante: nenhuma estrela
