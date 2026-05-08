import pygame


class MenuGameOver:

    def __init__(self, ancho, alto):

        self.ancho = ancho
        self.alto = alto

        self.font_titulo = pygame.font.SysFont("Arial", 80)
        self.font_texto = pygame.font.SysFont("Arial", 35)

    # ---------------------------------
    # INPUT
    # ---------------------------------
    def actualizar(self, eventos):

        for evento in eventos:

            if evento.type == pygame.KEYDOWN:

                # REINICIAR
                if evento.key == pygame.K_r:
                    return "reiniciar"

                # MENU
                if evento.key == pygame.K_m:
                    return "menu"

        return "game_over"

    # ---------------------------------
    # DIBUJAR
    # ---------------------------------
    def dibujar(self, pantalla):

        overlay = pygame.Surface(
            (self.ancho, self.alto),
            pygame.SRCALPHA
        )

        overlay.fill((0, 0, 0, 220))

        pantalla.blit(overlay, (0, 0))

        # TITULO
        titulo = self.font_titulo.render(
            "GAME OVER",
            True,
            (255, 50, 50)
        )

        pantalla.blit(
            titulo,
            (
                self.ancho // 2 - titulo.get_width() // 2,
                self.alto // 3
            )
        )

        # TEXTO
        texto = self.font_texto.render(
            "R = Reiniciar | M = Menu Principal",
            True,
            (255, 255, 255)
        )

        pantalla.blit(
            texto,
            (
                self.ancho // 2 - texto.get_width() // 2,
                self.alto // 2
            )
        )