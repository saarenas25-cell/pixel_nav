import pygame

class proyectiles:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def borrar(self, balas, ALTO):
        if self.y < -10:  
            balas.remove(self)