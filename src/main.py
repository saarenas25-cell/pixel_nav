import pygame
from players.jugador import Jugador

pygame.init()
reloj = pygame.time.Clock()
pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Pixel Nav") 

player = Jugador(pantalla.get_width() // 2, pantalla.get_height() // 2)
print (pantalla)

ejecutando = True
while ejecutando:
#Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False
        if evento.type == pygame.VIDEORESIZE:
            pantalla = pygame.display.set_mode((evento.w, evento.h), pygame.RESIZABLE)
    pantalla.fill((255, 255, 255))

#Lógica (movimiento, etc.)
    teclas = pygame.key.get_pressed()
    player.mover(teclas)
    player.limite_pantalla(pantalla.get_width(), pantalla.get_height())


#Dibujar
    player.dibujar(pantalla)
#flip()
    pygame.display.flip()
#tick()
    reloj.tick(60)

pygame.quit()
