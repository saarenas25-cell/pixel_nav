import pygame

class Jugador:
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.color = (0, 0, 255) 
        self.ancho = 30
        self.alto = 60

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
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))
    
    def limite_pantalla(self, ancho, alto):#limites de la pantalla 
        if self.x < (ancho*0.25) - self.ancho:
            self.x = (ancho*0.25) - self.ancho
        elif self.x > (ancho*0.75) - self.ancho:
            self.x = (ancho*0.75) - self.ancho
        if self.y < alto*0.25 - self.alto:
            self.y = alto*0.25 - self.alto
        elif self.y > alto - self.alto:
            self.y = alto - self.alto
