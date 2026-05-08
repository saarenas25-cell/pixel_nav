import pygame

class Jugador:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        # ---------------------------------
        # TAMAÑO DE LA NAVE
        # ---------------------------------
        self.ancho = 80
        self.alto = 80

        # ---------------------------------
        # CARGAR IMAGEN
        # ---------------------------------
        self.imagen = pygame.image.load(
            "assets/sprites/jugador/nave.png"
        ).convert_alpha()

        # ---------------------------------
        # ESCALAR IMAGEN
        # ---------------------------------
        self.imagen = pygame.transform.scale(
            self.imagen,
            (self.ancho, self.alto)
        )

        # ---------------------------------
        # VELOCIDAD
        # ---------------------------------
        self.velocidad = 5

    # ---------------------------------
    # MOVIMIENTO
    # ---------------------------------
    def mover(self, teclas):

        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidad

        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidad

        if teclas[pygame.K_UP]:
            self.y -= self.velocidad

        if teclas[pygame.K_DOWN]:
            self.y += self.velocidad

    # ---------------------------------
    # DIBUJAR JUGADOR
    # ---------------------------------
    def dibujar(self, pantalla):

        pantalla.blit(
            self.imagen,
            (self.x, self.y)
        )

    # ---------------------------------
    # LIMITES DE PANTALLA
    # ---------------------------------
    def limite_pantalla(self, ancho, alto):

        if self.x < (ancho * 0.25) - self.ancho:
            self.x = (ancho * 0.25) - self.ancho

        elif self.x > (ancho * 0.75) - self.ancho:
            self.x = (ancho * 0.75) - self.ancho

        if self.y < alto * 0.25 - self.alto:
            self.y = alto * 0.25 - self.alto

        elif self.y > alto - self.alto:
            self.y = alto - self.alto