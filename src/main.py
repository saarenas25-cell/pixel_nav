import pygame

from enemigos.enemigo_1 import Enemigo_1
from enemigos.enemigo_2 import Enemigo_2

from estados.estado_juego import EstadoJuego
from estados.gestor_estados import GestorEstados


# ---------------------------------
# INICIALIZAR PYGAME
# ---------------------------------
pygame.init()

# ---------------------------------
# CONFIGURACIÓN DE PANTALLA
# ---------------------------------
pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Pixel Nav")

ANCHO = pantalla.get_width()
ALTO = pantalla.get_height()
reloj = pygame.time.Clock()

# ---------------------------------
# CREAR ESTADO DEL JUEGO Y MENUS
# ---------------------------------

ejecutando = True

estado_juego = EstadoJuego(ANCHO, ALTO)
estado_juego.inicializar()

Gestor = GestorEstados(ejecutando, estado_juego)

# ---------------------------------
# BUCLE PRINCIPAL
# ---------------------------------
while ejecutando:

    eventos = pygame.event.get()

    # ---------------------------------
    # EVENTOS
    # ---------------------------------
    
    Gestor.actualizar(eventos)
    ejecutando = Gestor.actualizar(eventos)
    
    teclas = pygame.key.get_pressed()

    # =================================
    # MENU PRINCIPAL
    # =================================
    if estado_juego.estado == "menu":

        resultado = estado_juego.menu_principal.actualizar(eventos)

        if resultado == "jugar":
            estado_juego.estado = "juego"
        elif resultado == "salir":
            ejecutando = False

        estado_juego.menu_principal.dibujar(pantalla)

        pygame.display.flip()
        reloj.tick(60)
        continue

    # =================================
    # LÓGICA DEL JUEGO
    # solo se ejecuta cuando estado = "juego"
    # =================================
    if estado_juego.estado == "juego":

        # GENERAR ENEMIGOS
        Enemigo_1.generar_enemigo(estado_juego.Enemigos, ANCHO)
        Enemigo_2.generar_enemigo(estado_juego.Enemigos, ANCHO)

        # MOVER JUGADOR
        estado_juego.jugador.mover(teclas)
        estado_juego.jugador.limite_pantalla(ANCHO, ALTO)

        # MOVER Y BORRAR BALAS
        estado_juego.Gestor_balas()
        
        # MOVER Y BORRAR ENEMIGOS
        estado_juego.Gestor_enemigos()

        # COLISIONES
        estado_juego.puntaje += Enemigo_1.colision_balas(estado_juego.balas, estado_juego.Enemigos)
        estado_juego.vida += Enemigo_1.colision_jugador(estado_juego.jugador, estado_juego.Enemigos)

        # GAME OVER
        estado_juego.Game_Over()

        # RECARGAR ENERGÍA  
        estado_juego.Recargar_Energia()

    # =================================
    # DIBUJO — siempre en este orden:
    # 1. fondo, 2. enemigos, 3. jugador, 4. balas, 5. HUD
    # =================================

    # 1. FONDO
    pantalla.fill((100, 100, 100))

    # 2. ENEMIGOS
    estado_juego.Dibujar_Enemigo(pantalla)

    # 3. JUGADOR
    estado_juego.jugador.dibujar(pantalla)

    # 4. BALAS
    estado_juego.Dibujar_balas(pantalla)

    # 5. HUD
    estado_juego.hud.dibujar(pantalla)

    # =================================
    # MENÚS SUPERPUESTOS
    # se dibujan encima del juego cuando corresponde
    # =================================
    
    if estado_juego.estado == "pausa":
        estado_juego.menu_pausa.dibujar(pantalla)

    if estado_juego.estado == "game_over":
        estado_juego.menu_game_over.dibujar(pantalla)

    # ACTUALIZAR PANTALLA
    pygame.display.flip()
    reloj.tick(60)

# ---------------------------------
# CERRAR PYGAME
# ---------------------------------
pygame.quit()