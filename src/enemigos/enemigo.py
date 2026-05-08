# enemigo.py (clase padre)
import pygame
import time
import random

class Enemigo:
    ancho_enemigo = 30
    alto_enemigo = 60

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 255, 255)
        self.vida = 0

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho_enemigo, self.alto_enemigo))

    def borrar(self, Enemigos, ALTO):
        if self.y > (ALTO + self.alto_enemigo):
            Enemigos.remove(self)

    def mover(self, x_pantalla=None, y_pantalla=None):
        pass  # cada hijo lo implementa a su manera