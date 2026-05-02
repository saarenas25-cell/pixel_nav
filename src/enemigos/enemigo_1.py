import pygame
import random
import time

class Enemigo:

    ancho_enemigo = 30
    alto_enemigo = 60
    puntos = 5
    daño = -10

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
            Enemigos.append(Enemigo(random.randint(int(ANCHO*0.25)+(Enemigo.ancho_enemigo//2), 
                                                int(ANCHO*0.75)-(Enemigo.ancho_enemigo//2)), 
                                                (0 - Enemigo.alto_enemigo)))

    # ---------------------------------

    def mover(self):
        self.y += 2     
        
    def borrar(self, Enemigos, ALTO):
        if self.y > (ALTO + Enemigo.alto_enemigo):  
            Enemigos.remove(self)
    # ---------------------------------
    # generar COLISIONES CON BALAS Y DAR PUNTOS
    # ---------------------------------
       
    @staticmethod
    def colision_balas(balas, Enemigos):
        for bala in balas:
            for enemigo in Enemigos:
                if (bala.x < enemigo.x + Enemigo.ancho_enemigo and
                    bala.x + bala.ancho > enemigo.x and
                    bala.y < enemigo.y + Enemigo.alto_enemigo and
                    bala.y + bala.alto > enemigo.y):
                    balas.remove(bala)
                    Enemigos.remove(enemigo)
                    return Enemigo.puntos
        return 0
    
    # ---------------------------------
    
    # ---------------------------------
    # generar DAÑO cada 2 segundos si el jugador colisiona con el enemigo
    # ---------------------------------
    
    @staticmethod
    def inbulnerable_2s():
        timepo_actual = time.time()
        if timepo_actual - getattr(Enemigo, 'ultimo_daño', 0) > 2:
            Enemigo.ultimo_daño = timepo_actual
            return True
        return False
        
    @staticmethod
    def colision_jugador(jugador, Enemigos):
        for enemigo in Enemigos:
            if (jugador.x < enemigo.x + Enemigo.ancho_enemigo and
                jugador.x + jugador.ancho > enemigo.x and
                jugador.y < enemigo.y + Enemigo.alto_enemigo and
                jugador.y + jugador.alto > enemigo.y):
                if Enemigo.inbulnerable_2s():
                    return Enemigo.daño
        return 0
    
    # ---------------------------------
    
        

            