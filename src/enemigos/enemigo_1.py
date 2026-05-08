import pygame
import random
import time

class Enemigo:

    # ---------------------------------
    # CONFIGURACIÓN
    # ---------------------------------
    ancho_enemigo = 70
    alto_enemigo = 70

    puntos = 5
    daño = -10

    # ---------------------------------
    # CONSTRUCTOR
    # ---------------------------------
    def __init__(self, x, y):

        self.x = x
        self.y = y

        # ---------------------------------
        # CARGAR IMAGEN
        # ---------------------------------
        self.imagen = pygame.image.load(
            "assets/sprites/enemigos/enemigo_1.png"
        ).convert_alpha()

        # ---------------------------------
        # ESCALAR IMAGEN
        # ---------------------------------
        self.imagen = pygame.transform.scale(self.imagen,(Enemigo.ancho_enemigo,Enemigo.alto_enemigo))

    # ---------------------------------
    # ROTAR ENEMIGO
    # ---------------------------------
        self.imagen = pygame.transform.rotate(self.imagen,180)
    # ---------------------------------
    # DIBUJAR ENEMIGO
    # ---------------------------------
    def dibujar(self, pantalla):

        pantalla.blit(
            self.imagen,
            (self.x, self.y)
        )

    # ---------------------------------
    # GENERAR ENEMIGO CADA 5 SEGUNDOS
    # ---------------------------------
    @staticmethod
    def generar_5s():

        tiempo_actual = time.time()

        if tiempo_actual - getattr(
            Enemigo,
            'tiempo_ultimo_enemigo',
            0
        ) > 5:

            Enemigo.tiempo_ultimo_enemigo = tiempo_actual

            return True

        return False

    # ---------------------------------
    # GENERAR ENEMIGO
    # ---------------------------------
    @staticmethod
    def generar_enemigo(Enemigos, ANCHO):

        if Enemigo.generar_5s():

            nuevo_enemigo = Enemigo(

                random.randint(
                    int(ANCHO * 0.25) + (Enemigo.ancho_enemigo // 2),

                    int(ANCHO * 0.75) - (Enemigo.ancho_enemigo // 2)
                ),

                0 - Enemigo.alto_enemigo
            )

            Enemigos.append(nuevo_enemigo)

    # ---------------------------------
    # MOVIMIENTO
    # ---------------------------------
    def mover(self):

        self.y += 2

    # ---------------------------------
    # BORRAR ENEMIGO
    # ---------------------------------
    def borrar(self, Enemigos, ALTO):

        if self.y > (ALTO + Enemigo.alto_enemigo):

            Enemigos.remove(self)

    # ---------------------------------
    # COLISIONES CON BALAS
    # ---------------------------------
    @staticmethod
    def colision_balas(balas, Enemigos):

        for bala in balas:

            for enemigo in Enemigos:

                if (
                    bala.x < enemigo.x + Enemigo.ancho_enemigo and
                    bala.x + bala.ancho > enemigo.x and
                    bala.y < enemigo.y + Enemigo.alto_enemigo and
                    bala.y + bala.alto > enemigo.y
                ):

                    balas.remove(bala)
                    Enemigos.remove(enemigo)

                    return Enemigo.puntos

        return 0

    # ---------------------------------
    # INVULNERABILIDAD
    # ---------------------------------
    @staticmethod
    def inbulnerable_2s():

        tiempo_actual = time.time()

        if tiempo_actual - getattr(
            Enemigo,
            'ultimo_daño',
            0
        ) > 2:

            Enemigo.ultimo_daño = tiempo_actual

            return True

        return False

    # ---------------------------------
    # COLISION JUGADOR
    # ---------------------------------
    @staticmethod
    def colision_jugador(jugador, Enemigos):

        for enemigo in Enemigos:

            if (
                jugador.x < enemigo.x + Enemigo.ancho_enemigo and
                jugador.x + jugador.ancho > enemigo.x and
                jugador.y < enemigo.y + Enemigo.alto_enemigo and
                jugador.y + jugador.alto > enemigo.y
            ):

                if Enemigo.inbulnerable_2s():

                    return Enemigo.daño

        return 0
    # ---------------------------------
    
        

            