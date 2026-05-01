import pygame
import random
import time

class Enemigo:

    ancho_enemigo = 30
    alto_enemigo = 60

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 0, 0) 

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y,  Enemigo.ancho_enemigo, Enemigo.alto_enemigo))

    # ---------------------------------
    # generar enemigo cada 5 segundos
    # ---------------------------------

    @staticmethod
    def generar_5s():
        timepo_actual = time.time()
        if timepo_actual - getattr(Enemigo, 'tiempo_ultimo_enemigo', 0) > 5:
            Enemigo.tiempo_ultimo_enemigo = timepo_actual
            return True
        return False

    @staticmethod
    def generar_enemigo(Enemigos, ANCHO):
        if Enemigo.generar_5s():
            Enemigos.append(Enemigo(random.randint(int(ANCHO*0.25), int(ANCHO*0.75)), (0 - Enemigo.alto_enemigo)))

    # ---------------------------------

    def mover(self):
        self.y += 2  
        
    def borrar(self, Enemigos, ALTO):
        if self.y > (ALTO + Enemigo.alto_enemigo):  
            Enemigos.remove(self)
