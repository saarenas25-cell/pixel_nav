import pygame
from proyectiles.proyectiles import proyectiles

class Bala(proyectiles):
    def __init__(self, x, y, direccion=1, ancho=10, alto=10):
        super().__init__(x, y)
        self.color = (255, 0, 0)
        self.velocidad = 10
        self.direccion = direccion
        self.ancho = ancho
        self.alto = alto
        self.x = self.x - (self.ancho //2)


    def mover(self):
        self.y -= self.velocidad * self.direccion

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))



