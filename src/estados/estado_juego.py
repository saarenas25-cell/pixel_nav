import pygame

from players.hud import HUD
from players.jugador import Jugador

from ui.menu_principal import MenuPrincipal
from ui.menu_pausa import MenuPausa
from ui.menu_game_over import MenuGameOver

from proyectiles.bala import Bala

class EstadoJuego:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.estado = "menu"
    
    def inicializar(self):
        self.jugador = Jugador(self.ancho // 2, self.alto // 2)
        self.hud = HUD(self, self.ancho, self.alto)
        self.balas = []
        self.Enemigos = []
        self.vida = 100
        self.energia = 100
        self.puntaje = 0
        self.monedas = 0
        self.menu_principal = MenuPrincipal(self.ancho, self.alto)
        self.menu_pausa = MenuPausa(self.ancho, self.alto)
        self.menu_game_over = MenuGameOver(self.ancho, self.alto)
        
    def Game_Over(self):
        if self.vida == 0:
            self.estado = "game_over"
            
    def Recargar_Energia(self):
        if self.energia < 100:
            self.energia += 0.1
            
    def Gestor_enemigos(self):
        for enemigo in self.Enemigos[:]:
            enemigo.mover(self.ancho, self.alto)
            enemigo.borrar(self.Enemigos, self.alto)
            
    def Dibujar_Enemigo(self, pantalla):
        for enemigo in self.Enemigos:
            enemigo.dibujar(pantalla)
            
    def Gestor_balas(self):
        for bala in self.balas[:]:
            bala.mover()
            bala.borrar(self.balas, self.alto)
        
    def Dibujar_balas(self, pantalla):
        for bala in self.balas:
            bala.dibujar(pantalla)
        
    def Disparar(self):
        self.energia, disparo = Bala.municion_gastada(self.energia)
        if disparo:
            nueva_bala = Bala(self.jugador.x + self.jugador.ancho // 2,self.jugador.y)
            self.balas.append(nueva_bala)
        