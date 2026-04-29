import pygame
import time

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (200, 60, 60)
VERDE = (60, 200, 120)
AZUL = (80, 140, 255)
GRIS = (60, 60, 60)


class HUD:
    def __init__(self, ancho=800, alto=600):
        pygame.font.init()

        # Pantalla
        self.ancho = ancho
        self.alto = alto

        # Fuentes
        self.font_small = pygame.font.SysFont("Arial", 18)
        self.font_medium = pygame.font.SysFont("Arial", 24)
        self.font_big = pygame.font.SysFont("Arial", 48)

        # Variables
        self.vida = 100
        self.vida_max = 100
        self.vida_suavizada = 100

        self.energia = 100
        self.energia_max = 100

        self.puntaje = 0
        self.monedas = 0

        self.tiempo_inicio = time.time()

        self.mensaje = ""
        self.mensaje_tiempo = 0

    # =========================
    # ACTUALIZAR
    # =========================
    def actualizar(self, vida=100, energia=100, puntaje=0, monedas=0):
        self.vida = max(0, min(self.vida_max, vida))
        self.energia = max(0, min(self.energia_max, energia))
        self.puntaje = puntaje
        self.monedas = monedas

        # Animación suave de vida
        self.vida_suavizada += (self.vida - self.vida_suavizada) * 0.1

    # =========================
    # MENSAJES
    # =========================
    def mostrar_mensaje(self, texto, duracion=2):
        self.mensaje = texto
        self.mensaje_tiempo = time.time() + duracion

    # =========================
    # DIBUJO
    # =========================
    def dibujar_barra(self, pantalla, x, y, w, h, valor, max_valor, color):
        pygame.draw.rect(pantalla, GRIS, (x, y, w, h))
        ancho = (valor / max_valor) * w
        pygame.draw.rect(pantalla, color, (x, y, ancho, h))
        pygame.draw.rect(pantalla, NEGRO, (x, y, w, h), 2)

    def dibujar_texto(self, pantalla, texto, x, y, fuente, color=BLANCO):
        surf = fuente.render(texto, True, color)
        pantalla.blit(surf, (x, y))

    def dibujar(self, pantalla):
        # Barras
        self.dibujar_barra(pantalla, 20, 20, 200, 20, self.vida_suavizada, self.vida_max, ROJO)
        self.dibujar_barra(pantalla, 20, 50, 200, 15, self.energia, self.energia_max, AZUL)

        # Texto
        self.dibujar_texto(pantalla, f"Vida: {int(self.vida)}", 230, 18, self.font_small)
        self.dibujar_texto(pantalla, f"Energia: {int(self.energia)}", 230, 48, self.font_small)

        self.dibujar_texto(pantalla, f"Puntaje: {int(self.puntaje)}", 20, 80, self.font_medium)
        self.dibujar_texto(pantalla, f"Monedas: {self.monedas}", 20, 110, self.font_medium)

        # Tiempo
        tiempo = int(time.time() - self.tiempo_inicio)
        self.dibujar_texto(pantalla, f"Tiempo: {tiempo}s", 20, 140, self.font_small)

        # Mensaje central
        if self.mensaje and time.time() < self.mensaje_tiempo:
            texto = self.font_big.render(self.mensaje, True, BLANCO)
            rect = texto.get_rect(center=(self.ancho // 2, self.alto // 2))
            pantalla.blit(texto, rect)