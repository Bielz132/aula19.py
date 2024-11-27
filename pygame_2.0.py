import pygame, sys
from pygame.locals import QUIT
pygame.init()

largura, altura = 600,500
tela = pygame.display.set_mode((largura, altura))

branca = (255,255,255)
vermelho = (255,0,0)

x, y = largura//2, altura//2
tamanho = 30
velocidade = 5

carregando = True
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.quit:
            carregando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x-=velocidade
    if teclas[pygame.K_RIGHT]:
        x+=velocidade
    if teclas[pygame.K_UP]:
        y-=velocidade
    if teclas[pygame.K_DOWN]:
        y+=velocidade

    tela.fill(branca)
    pygame.draw.rect(tela, vermelho, (x,y, tamanho, tamanho))

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
    
