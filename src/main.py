import pygame

from players.jugador import Jugador
from players.hud import HUD
from proyectiles.bala import Bala
from enemigos.enemigo_1 import Enemigo
from efectos.explosion import Explosion

from ui.menus.menu_principal import MenuPrincipal
from ui.menus.menu_pausa import MenuPausa
from ui.menus.menu_game_over import MenuGameOver


def main():

    # ---------------------------------
    # INICIALIZAR
    # ---------------------------------
    pygame.init()

    pantalla = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Pixel Nav")

    ANCHO = pantalla.get_width()
    ALTO = pantalla.get_height()

    reloj = pygame.time.Clock()

    # ---------------------------------
    # FONDO
    # ---------------------------------
    background = pygame.image.load(
        "assets/backgrounds/espacio.png"
    )

    background = pygame.transform.scale(
        background,
        (ANCHO, ALTO)
    )

    # ---------------------------------
    # MENUS
    # ---------------------------------
    menu = MenuPrincipal(ANCHO, ALTO)
    menu_pausa = MenuPausa(ANCHO, ALTO)
    menu_game_over = MenuGameOver(ANCHO, ALTO)

    # ---------------------------------
    # ESTADO
    # ---------------------------------
    estado_juego = "menu"

    # ---------------------------------
    # REINICIAR JUEGO
    # ---------------------------------
    def reiniciar_juego():

        jugador = Jugador(ANCHO // 2, ALTO // 2)
        hud = HUD(ANCHO, ALTO)

        balas = []
        Enemigos = []
        explosiones = []

        vida = 100
        energia = 100
        puntaje = 0
        monedas = 0

        return (
            jugador,
            hud,
            balas,
            Enemigos,
            explosiones,
            vida,
            energia,
            puntaje,
            monedas
        )

    # ---------------------------------
    # CREAR OBJETOS
    # ---------------------------------
    (
        jugador,
        hud,
        balas,
        Enemigos,
        explosiones,
        vida,
        energia,
        puntaje,
        monedas
    ) = reiniciar_juego()

    ejecutando = True

    # ---------------------------------
    # LOOP PRINCIPAL
    # ---------------------------------
    while ejecutando:

        eventos = pygame.event.get()

        # =================================
        # EVENTOS
        # =================================
        for evento in eventos:

            if evento.type == pygame.QUIT:
                ejecutando = False

            if evento.type == pygame.KEYDOWN:

                # =========================
                # MENU
                # =========================
                if estado_juego == "menu":

                    if evento.key == pygame.K_ESCAPE:
                        ejecutando = False

                # =========================
                # JUEGO
                # =========================
                elif estado_juego == "juego":

                    # PAUSA
                    if evento.key == pygame.K_ESCAPE:
                        estado_juego = "pausa"

                    # DISPARO
                    if evento.key == pygame.K_SPACE:

                        energia = Bala.municion_gastada(energia)

                        balas.append(
                            Bala(
                                jugador.x + jugador.ancho // 2,
                                jugador.y
                            )
                        )

                # =========================
                # PAUSA
                # =========================
                elif estado_juego == "pausa":

                    # CONTINUAR
                    if evento.key == pygame.K_ESCAPE:
                        estado_juego = "juego"

                    # REINICIAR
                    if evento.key == pygame.K_r:

                        (
                            jugador,
                            hud,
                            balas,
                            Enemigos,
                            explosiones,
                            vida,
                            energia,
                            puntaje,
                            monedas
                        ) = reiniciar_juego()

                        estado_juego = "juego"

                    # MENU
                    if evento.key == pygame.K_m:

                        (
                            jugador,
                            hud,
                            balas,
                            Enemigos,
                            explosiones,
                            vida,
                            energia,
                            puntaje,
                            monedas
                        ) = reiniciar_juego()

                        estado_juego = "menu"

                # =========================
                # GAME OVER
                # =========================
                elif estado_juego == "game_over":

                    # REINICIAR
                    if evento.key == pygame.K_r:

                        (
                            jugador,
                            hud,
                            balas,
                            Enemigos,
                            explosiones,
                            vida,
                            energia,
                            puntaje,
                            monedas
                        ) = reiniciar_juego()

                        estado_juego = "juego"

                    # MENU
                    if evento.key == pygame.K_m:

                        (
                            jugador,
                            hud,
                            balas,
                            Enemigos,
                            explosiones,
                            vida,
                            energia,
                            puntaje,
                            monedas
                        ) = reiniciar_juego()

                        estado_juego = "menu"

        teclas = pygame.key.get_pressed()

        # =================================
        # MENU PRINCIPAL
        # =================================
        if estado_juego == "menu":

            resultado = menu.actualizar(eventos)

            if resultado == "jugar":
                estado_juego = "juego"

            elif resultado == "salir":
                ejecutando = False

            menu.dibujar(pantalla)

            pygame.display.flip()
            reloj.tick(60)

            continue

        # =================================
        # JUEGO
        # =================================
        if estado_juego == "juego":

            # ENEMIGOS
            Enemigo.generar_enemigo(Enemigos, ANCHO)

            # JUGADOR
            jugador.mover(teclas)
            jugador.limite_pantalla(ANCHO, ALTO)

            # ENEMIGOS
            for enemigo in Enemigos:
                enemigo.mover()
                enemigo.borrar(Enemigos, ALTO)

            # BALAS
            for bala in balas:
                bala.mover()
                bala.borrar(balas, ALTO)

            # ---------------------------------
            # COLISIONES
            # ---------------------------------
            balas_a_eliminar = []
            enemigos_a_eliminar = []

            for bala in balas:
                for enemigo in Enemigos:

                    if (
                        bala.x < enemigo.x + Enemigo.ancho_enemigo and
                        bala.x + bala.ancho > enemigo.x and
                        bala.y < enemigo.y + Enemigo.alto_enemigo and
                        bala.y + bala.alto > enemigo.y
                    ):

                        explosiones.append(
                            Explosion(enemigo.x, enemigo.y)
                        )

                        balas_a_eliminar.append(bala)
                        enemigos_a_eliminar.append(enemigo)

                        puntaje += Enemigo.puntos

            for b in balas_a_eliminar:
                if b in balas:
                    balas.remove(b)

            for e in enemigos_a_eliminar:
                if e in Enemigos:
                    Enemigos.remove(e)

            # ---------------------------------
            # COLISION JUGADOR
            # ---------------------------------
            vida += Enemigo.colision_jugador(
                jugador,
                Enemigos
            )

            # ---------------------------------
            # GAME OVER
            # ---------------------------------
            if vida <= 0:
                vida = 0
                estado_juego = "game_over"

            # ---------------------------------
            # ENERGIA
            # ---------------------------------
            if energia < 100:
                energia += 0.1

            # ---------------------------------
            # EXPLOSIONES
            # ---------------------------------
            for exp in explosiones:
                exp.update()

            explosiones = [
                exp for exp in explosiones
                if not exp.terminada
            ]

        # =================================
        # DIBUJAR JUEGO
        # =================================
        pantalla.blit(background, (0, 0))

        jugador.dibujar(pantalla)

        for enemigo in Enemigos:
            enemigo.dibujar(pantalla)

        for bala in balas:
            bala.dibujar(pantalla)

        for exp in explosiones:
            exp.dibujar(pantalla)

        hud.actualizar(
            vida=vida,
            energia=energia,
            puntaje=puntaje,
            monedas=monedas
        )

        hud.dibujar(pantalla)

        # =================================
        # PAUSA
        # =================================
        if estado_juego == "pausa":
            menu_pausa.dibujar(pantalla)

        # =================================
        # GAME OVER
        # =================================
        if estado_juego == "game_over":
            menu_game_over.dibujar(pantalla)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()