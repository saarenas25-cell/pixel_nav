import pygame

class Jugador:
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.color = (0, 0, 255) 

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.x -= 5
        if teclas[pygame.K_RIGHT]:
            self.x += 5
        if teclas[pygame.K_UP]:
            self.y -= 5
        if teclas[pygame.K_DOWN]:
            self.y += 5

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, 50, 50))
    
    def limite_pantalla(self, ancho, alto):#limites de la pantalla 
        if self.x < ((ancho/2)-((ancho/2)*0.5)) - 50:
            self.x = ((ancho/2)-((ancho/2)*0.5)) - 50
        elif self.x > (ancho/2)+((ancho/2)*0.5) - 50:
            self.x = (ancho/2)+((ancho/2)*0.5) - 50
        if self.y < 0:
            self.y = 0
        elif self.y > alto - 50:
            self.y = alto - 50
