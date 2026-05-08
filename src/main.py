import pygame
from players.jugador import Jugador 
from players.hud import HUD
from proyectiles.bala import Bala
from enemigos.enemigo_1 import Enemigo_1
from enemigos.enemigo_2 import Enemigo_2

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
# CREAR OBJETOS
# ---------------------------------
jugador = Jugador(ANCHO // 2, ALTO // 2)
hud = HUD(ANCHO, ALTO)

balas = []
Enemigos = []

# ---------------------------------
# VARIABLES DEL JUEGO
# ---------------------------------
vida = 100
energia = 100
puntaje = 0
monedas = 0

ejecutando = True

# ---------------------------------
# BUCLE PRINCIPAL
# ---------------------------------
while ejecutando:

    # ---------------------------------
    # EVENTOS (cosas que pasan una sola vez, como presionar una tecla)
    # ---------------------------------
    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            ejecutando = False

        elif evento.type == pygame.KEYDOWN:

            # SALIR
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

            # DISPARAR + GASTAR ENERGÍA
            if evento.key == pygame.K_SPACE:
                energia = Bala.municion_gastada(energia)
                nueva_bala = Bala(jugador.x + jugador.ancho // 2, jugador.y)
                balas.append(nueva_bala)

            # SUMAR MONEDA (PRUEBA)
            if evento.key == pygame.K_k:
                monedas += 1

    # ---------------------------------
    # TECLAS PRESIONADAS (movimiento continuo)
    # ---------------------------------
    teclas = pygame.key.get_pressed()

    # ---------------------------------
    # GENERAR ENEMIGOS
    # cada clase maneja su propio timer interno
    # ---------------------------------
    Enemigo_1.generar_enemigo(Enemigos, ANCHO)
    Enemigo_2.generar_enemigo(Enemigos, ANCHO)

    # ---------------------------------
    # MOVER JUGADOR Y APLICAR LÍMITES DE PANTALLA
    # ---------------------------------
    jugador.mover(teclas)
    jugador.limite_pantalla(ANCHO, ALTO)

    # ---------------------------------
    # MOVER Y BORRAR BALAS
    # ---------------------------------
    for bala in balas[:]:
        bala.mover()
        bala.borrar(balas, ALTO)

    # ---------------------------------
    # MOVER Y BORRAR ENEMIGOS
    # Enemigo_2 necesita ANCHO y ALTO para saber dónde detenerse
    # Enemigo_1 solo se mueve hacia abajo sin parámetros
    # ---------------------------------
    for enemigo in Enemigos[:]:
        enemigo.mover(ANCHO, ALTO)  # cada uno sabe cómo moverse
        enemigo.borrar(Enemigos, ALTO)

    # ---------------------------------
    # COLISIONES
    # se calculan antes de dibujar para que el estado sea correcto
    # ---------------------------------
    puntaje += Enemigo_1.colision_balas(balas, Enemigos)
    vida += Enemigo_1.colision_jugador(jugador, Enemigos)

    # ---------------------------------
    # ACTUALIZAR ENERGÍA (se recarga sola con el tiempo)
    # ---------------------------------
    if energia < 100:
        energia += 0.1

    # ---------------------------------
    # EVITAR QUE VIDA BAJE DE 0
    # ---------------------------------
    if vida < 0:
        vida = 0

    # ---------------------------------
    # ACTUALIZAR HUD con los valores actuales
    # ---------------------------------
    hud.actualizar(
        vida=vida,
        energia=energia,
        puntaje=puntaje,
        monedas=monedas
    )

    # =================================
    # DIBUJO — siempre en este orden:
    # 1. fondo, 2. enemigos, 3. jugador, 4. balas, 5. HUD
    # el HUD va al final para quedar encima de todo
    # =================================

    # 1. LIMPIAR PANTALLA con el color de fondo
    pantalla.fill((100, 100, 100))

    # 2. DIBUJAR ENEMIGOS
    # como están en una sola lista, cada objeto dibuja con su propio color
    for enemigo in Enemigos:
        enemigo.dibujar(pantalla)

    # 3. DIBUJAR JUGADOR
    jugador.dibujar(pantalla)

    # 4. DIBUJAR BALAS
    for bala in balas:
        bala.dibujar(pantalla)

    # 5. DIBUJAR HUD (encima de todo)
    hud.dibujar(pantalla)

    # ---------------------------------
    # ACTUALIZAR PANTALLA
    # muestra todo lo que se dibujó en este frame
    # ---------------------------------
    pygame.display.flip()
    reloj.tick(60)

# ---------------------------------
# CERRAR PYGAME al salir del bucle
# ---------------------------------
pygame.quit()