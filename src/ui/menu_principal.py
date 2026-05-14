import pygame


class MenuPrincipal:

    def __init__(self, ancho, alto):

        self.ancho = ancho
        self.alto = alto

        self.font_grande = pygame.font.SysFont("Arial", 80)
        self.font_pequeña = pygame.font.SysFont("Arial", 30)

    # ---------------------------------
    # MANEJAR INPUT
    # ---------------------------------
    def actualizar(self, eventos):

        for evento in eventos:

            if evento.type == pygame.KEYDOWN:

                # ENTER = jugar
                if evento.key == pygame.K_RETURN:
                    return "jugar"

                # ESC = salir
                if evento.key == pygame.K_ESCAPE:
                    return "salir"

        return "menu"

    # ---------------------------------
    # DIBUJAR MENÚ
    # ---------------------------------
    def dibujar(self, pantalla):

        pantalla.fill((0, 0, 0))

        # TÍTULO
        titulo = self.font_grande.render(
            "PIXEL NAV",
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

        # INSTRUCCIÓN
        texto = self.font_pequeña.render(
            "ENTER para jugar | ESC para salir",
            True,
            (200, 200, 200)
        )

        pantalla.blit(
            texto,
            (
                self.ancho // 2 - texto.get_width() // 2,
                self.alto // 2
            )
        )
        
