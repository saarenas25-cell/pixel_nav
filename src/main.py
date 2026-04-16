import pygame

pygame.init()

pantalla = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Pixel Nav") 

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.VIDEORESIZE:
            pantalla = pygame.display.set_mode((evento.w, evento.h), pygame.RESIZABLE)
    pantalla.fill((255, 255, 255))
    pygame.display.flip()
pygame.quit()