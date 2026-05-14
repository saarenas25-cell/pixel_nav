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

    def __init__(self, estado_juego, ancho=800, alto=600):

        pygame.font.init()

        # Referencia al juego
        self.estado_juego = estado_juego

        # Pantalla
        self.ancho = ancho
        self.alto = alto

        # Fuentes
        self.font_small = pygame.font.SysFont("Arial", 18)
        self.font_medium = pygame.font.SysFont("Arial", 24)
        self.font_big = pygame.font.SysFont("Arial", 48)

        # Configuración visual
        self.vida_max = 100
        self.energia_max = 100

        # Animaciones visuales
        self.vida_suavizada = 100

        # Tiempo
        self.tiempo_inicio = time.time()

        # Mensajes
        self.mensaje = ""
        self.mensaje_tiempo = 0

    # =========================
    # MENSAJES
    # =========================
    def mostrar_mensaje(self, texto, duracion=2):

        self.mensaje = texto
        self.mensaje_tiempo = time.time() + duracion

    # =========================
    # DIBUJAR BARRAS
    # =========================
    def dibujar_barra(
        self,
        pantalla,
        x,
        y,
        w,
        h,
        valor,
        max_valor,
        color
    ):

        pygame.draw.rect(pantalla, GRIS, (x, y, w, h))

        ancho = (valor / max_valor) * w

        pygame.draw.rect(
            pantalla,
            color,
            (x, y, ancho, h)
        )

        pygame.draw.rect(
            pantalla,
            NEGRO,
            (x, y, w, h),
            2
        )

    # =========================
    # DIBUJAR TEXTO
    # =========================
    def dibujar_texto(
        self,
        pantalla,
        texto,
        x,
        y,
        fuente,
        color=BLANCO
    ):

        surf = fuente.render(texto, True, color)

        pantalla.blit(surf, (x, y))

    # =========================
    # DIBUJAR HUD
    # =========================
    def dibujar(self, pantalla):

        # Datos del juego
        vida = self.estado_juego.vida
        energia = self.estado_juego.energia
        puntaje = self.estado_juego.puntaje
        monedas = self.estado_juego.monedas

        # Animación suave de vida
        self.vida_suavizada += (
            vida - self.vida_suavizada
        ) * 0.1

        # =========================
        # BARRAS
        # =========================

        self.dibujar_barra(
            pantalla,
            20,
            20,
            200,
            20,
            self.vida_suavizada,
            self.vida_max,
            ROJO
        )

        self.dibujar_barra(
            pantalla,
            20,
            50,
            200,
            15,
            energia,
            self.energia_max,
            AZUL
        )

        # =========================
        # TEXTO
        # =========================

        self.dibujar_texto(
            pantalla,
            f"Vida: {int(vida)}",
            230,
            18,
            self.font_small
        )

        self.dibujar_texto(
            pantalla,
            f"Energia: {int(energia)}",
            230,
            48,
            self.font_small
        )

        self.dibujar_texto(
            pantalla,
            f"Puntaje: {int(puntaje)}",
            20,
            80,
            self.font_medium
        )

        self.dibujar_texto(
            pantalla,
            f"Monedas: {monedas}",
            20,
            110,
            self.font_medium
        )

        # =========================
        # TIEMPO
        # =========================

        tiempo = int(time.time() - self.tiempo_inicio)

        self.dibujar_texto(
            pantalla,
            f"Tiempo: {tiempo}s",
            20,
            140,
            self.font_small
        )

        # =========================
        # MENSAJE CENTRAL
        # =========================

        if (
            self.mensaje and
            time.time() < self.mensaje_tiempo
        ):

            texto = self.font_big.render(
                self.mensaje,
                True,
                BLANCO
            )

            rect = texto.get_rect(
                center=(
                    self.ancho // 2,
                    self.alto // 2
                )
            )

            pantalla.blit(texto, rect)