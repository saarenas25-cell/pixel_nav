import pygame
from players.jugador import Jugador 
from players.hud import HUD
from proyectiles.bala import Bala
from enemigos.enemigo_1 import Enemigo

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
aleatorio_enemigo = 0
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
    # EVENTOS
    # ---------------------------------
    for evento in pygame.event.get():

        

        if evento.type == pygame.QUIT:
            ejecutando = False

        elif evento.type == pygame.KEYDOWN:

            # SALIR
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

            # DISPARAR + ENERGÍA
            if evento.key == pygame.K_SPACE:
                energia = Bala.municion_gastada(energia)
                nueva_bala = Bala(jugador.x + jugador.ancho // 2,jugador.y)
                balas.append(nueva_bala)
            
            # BAJAR VIDA (PRUEBA)
            if evento.key == pygame.K_h:
                vida -= 10

            # SUBIR PUNTAJE (PRUEBA)
            if evento.key == pygame.K_j:
                puntaje += 50

            # SUMAR MONEDA (PRUEBA)
            if evento.key == pygame.K_k:
                monedas += 1

    # ---------------------------------
    # TECLAS PRESIONADAS
    # ---------------------------------
    teclas = pygame.key.get_pressed()

    # ---------------------------------
    # generacion de enemigos
    # ---------------------------------

    Enemigo.generar_enemigo(Enemigos, ANCHO)

    # ---------------------------------
    # MOVIMIENTO DEL JUGADOR Y ENEMIGOS
    # ---------------------------------
    jugador.mover(teclas)
    jugador.limite_pantalla(pantalla.get_width(),pantalla.get_height())

    # ---------------------------------
    # ACTUALIZAR ENEMIGOS
    # ---------------------------------
    for enemigo in Enemigos:
        enemigo.mover()
        enemigo.borrar(Enemigos, ANCHO)

    # ---------------------------------
    # ACTUALIZAR BALAS
    # ---------------------------------
    for bala in balas:
        bala.mover()
        bala.borrar(balas, ALTO)
        
    
    print(f"Balas: {len(balas)} | Enemigos: {len(Enemigos)}")

    # ---------------------------------
    # ACTUALIZAR ENERGÍA
    # ---------------------------------
    
    if energia < 100:
        energia += 0.1

    if vida < 0:
        vida = 0

    # ---------------------------------
    # ACTUALIZAR HUD
    # ---------------------------------
    hud.actualizar(
        vida=vida,
        energia=energia,
        puntaje=puntaje,
        monedas=monedas
    )

    # ---------------------------------
    # DIBUJAR FONDO
    # ---------------------------------
    pantalla.fill((100, 100, 100))

    # ---------------------------------
    # DIBUJAR JUGADOR Y ENEMIGOS
    # ---------------------------------
    jugador.dibujar(pantalla)

    for enemigo in Enemigos:
        enemigo.dibujar(pantalla) 

    # ---------------------------------
    # DIBUJAR BALAS
    # ---------------------------------
    for bala in balas:
        bala.dibujar(pantalla)

    # ---------------------------------
    # DIBUJAR HUD
    # ---------------------------------
    hud.dibujar(pantalla)

    # ---------------------------------
    # ACTUALIZAR PANTALLA
    # ---------------------------------
    pygame.display.flip()
    reloj.tick(60)

# ---------------------------------
# CERRAR JUEGO
# ---------------------------------
pygame.quit()