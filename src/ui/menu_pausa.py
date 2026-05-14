import pygame

class MenuPausa:

    def __init__(self, ancho, alto):

        self.ancho = ancho
        self.alto = alto

        self.font_titulo = pygame.font.SysFont("Arial", 70)
        self.font_opciones = pygame.font.SysFont("Arial", 35)

    # ---------------------------------
    # INPUT
    # ---------------------------------
    def actualizar(self, eventos):

        for evento in eventos:

            if evento.type == pygame.KEYDOWN:

                # CONTINUAR
                if evento.key == pygame.K_ESCAPE:
                    return "continuar"

                # REINICIAR
                if evento.key == pygame.K_r:
                    return "reiniciar"

                # VOLVER AL MENU
                if evento.key == pygame.K_m:
                    return "menu"

        return "pausa"

    # ---------------------------------
    # DIBUJAR
    # ---------------------------------
    def dibujar(self, pantalla):

        # capa oscura transparente
        overlay = pygame.Surface(
            (self.ancho, self.alto),
            pygame.SRCALPHA
        )

        overlay.fill((0, 0, 0, 180))

        pantalla.blit(overlay, (0, 0))

        # TITULO
        titulo = self.font_titulo.render(
            "PAUSA",
            True,
            (255, 255, 255)
        )

        pantalla.blit(
            titulo,
            (
                self.ancho // 2 - titulo.get_width() // 2,
                self.alto // 3
            )
        )

        # OPCIONES
        texto = self.font_opciones.render(
            "ESC = Continuar | R = Reiniciar | M = Menu",
            True,
            (220, 220, 220)
        )

        pantalla.blit(
            texto,
            (
                self.ancho // 2 - texto.get_width() // 2,
                self.alto // 2
            )
        )