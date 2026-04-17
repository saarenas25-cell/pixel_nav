import pygame
from players.jugador import Jugador

pygame.init()
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Pixel Nav") 

player = Jugador(100, 100)

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.VIDEORESIZE:
            pantalla = pygame.display.set_mode((evento.w, evento.h), pygame.RESIZABLE)
    pantalla.fill((255, 255, 255))
#Eventos
    
#Lógica (movimiento, etc.)
    teclas = pygame.key.get_pressed()
    player.mover(teclas)
#Dibujar
    player.dibujar(pantalla)
#flip()
    pygame.display.flip()
#tick()
    reloj.tick(60)

pygame.quit()
