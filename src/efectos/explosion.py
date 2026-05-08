import pygame

class Explosion:

    def __init__(self, x, y):

        self.x = x
        self.y = y

        # ---------------------------------
        # CARGAR FRAMES DE EXPLOSIÓN
        # ---------------------------------
        self.frames = []

        for i in range(1, 9):

            img = pygame.image.load(
                f"assets/sprites/explosion/explosion_{i}.png"
            ).convert_alpha()

            # ---------------------------------
            # AUMENTAR TAMAÑO DE LA EXPLOSIÓN
            # ---------------------------------
            img = pygame.transform.scale(
                img,
                (130, 130)   # 👈 más grande y visible
            )

            self.frames.append(img)

        # ---------------------------------
        # CONTROL DE ANIMACIÓN
        # ---------------------------------
        self.frame_actual = 0
        self.contador = 0
        self.velocidad = 2  # más bajo = más rápido

        self.terminada = False

    # ---------------------------------
    # ACTUALIZAR ANIMACIÓN
    # ---------------------------------
    def update(self):

        self.contador += 1

        if self.contador >= self.velocidad:

            self.contador = 0
            self.frame_actual += 1

            # terminar animación
            if self.frame_actual >= len(self.frames):
                self.terminada = True

    # ---------------------------------
    # DIBUJAR EXPLOSIÓN
    # ---------------------------------
    def dibujar(self, pantalla):

        if not self.terminada:

            pantalla.blit(
                self.frames[self.frame_actual],
                (self.x, self.y)
            )