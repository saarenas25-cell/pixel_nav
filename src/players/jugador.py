import pygame

class Jugador:
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.color = (0, 0, 255) 

    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.x -= 5
            if self.x < 0:
                self.x = 0
        if teclas[pygame.K_RIGHT]:
            self.x += 5
            if self.x > 670:
                self.x = 670
        """if teclas[pygame.K_UP]:
            self.y -= 5
        if teclas[pygame.K_DOWN]:
            self.y += 5"""

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, 50, 50))
