# enemigo_1.py
import time
import random
from .enemigo import Enemigo

class Enemigo_1(Enemigo):
    puntos = 5
    daño = -10
    vida = 20

    def __init__(self, x, y):
        super().__init__(x, y)
        self.color = (255, 0, 0)  # rojo
        self.vida = Enemigo_1.vida

    def mover(self, x_pantalla=None, y_pantalla=None):
        self.y += 2

    @staticmethod
    def generar_5s():
        tiempo_actual = time.time()
        if tiempo_actual - getattr(Enemigo_1, 'tiempo_ultimo_enemigo', 0) > 5:
            Enemigo_1.tiempo_ultimo_enemigo = tiempo_actual
            return True
        return False

    @staticmethod
    def generar_enemigo(Enemigos, ANCHO):
        if Enemigo_1.generar_5s():
            Enemigos.append(Enemigo_1(
                random.randint(
                    int(ANCHO*0.25) + (Enemigo_1.ancho_enemigo//2),
                    int(ANCHO*0.75) - (Enemigo_1.ancho_enemigo//2)
                ),
                (0 - Enemigo_1.alto_enemigo)
            ))

    @staticmethod
    def colision_balas(balas, Enemigos):
        for bala in balas[:]:
            for enemigo in Enemigos[:]:
                if (bala.x < enemigo.x + enemigo.ancho_enemigo and
                    bala.x + bala.ancho > enemigo.x and
                    bala.y < enemigo.y + enemigo.alto_enemigo and
                    bala.y + bala.alto > enemigo.y):
                    balas.remove(bala)
                    enemigo.vida -= 10
                    if enemigo.vida <= 0:
                        Enemigos.remove(enemigo)
                    return enemigo.puntos  # ← usa los puntos del enemigo que fue golpeado
        return 0

    @staticmethod
    def colision_jugador(jugador, Enemigos):
        tiempo_actual = time.time()
        if tiempo_actual - getattr(Enemigo_1, 'ultimo_daño', 0) > 2:
            for enemigo in Enemigos:
                if (jugador.x < enemigo.x + enemigo.ancho_enemigo and
                    jugador.x + jugador.ancho > enemigo.x and
                    jugador.y < enemigo.y + enemigo.alto_enemigo and
                    jugador.y + jugador.alto > enemigo.y):
                    Enemigo_1.ultimo_daño = tiempo_actual
                    return enemigo.daño  # ← usa el daño del enemigo que colisionó
        return 0