# enemigo_2.py
import time
import random
from .enemigo import Enemigo

class Enemigo_2(Enemigo):
    puntos = 10
    daño = -20
    vida = 30

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (0, 255, 0)  # verde
        self.vida = Enemigo_2.vida

    def mover(self, x_pantalla=None, y_pantalla=None):
        if y_pantalla and self.y < y_pantalla * 0.25:
            self.y += 1

    @staticmethod
    def generar_5s():
        tiempo_actual = time.time()
        if tiempo_actual - getattr(Enemigo_2, 'tiempo_ultimo_enemigo', 0) > 8:  # cada 8s
            Enemigo_2.tiempo_ultimo_enemigo = tiempo_actual
            return True
        return False

    @staticmethod
    def generar_enemigo(Enemigos, ANCHO):
        if Enemigo_2.generar_5s():
            Enemigos.append(Enemigo_2(
                random.randint(
                    int(ANCHO*0.25) + (Enemigo_2.ancho_enemigo//2),
                    int(ANCHO*0.75) - (Enemigo_2.ancho_enemigo//2)
                ),
                (0 - Enemigo_2.alto_enemigo)
            ))