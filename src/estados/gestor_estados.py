import pygame


class GestorEstados:
    def __init__(self, ejecutando, estado_juego):
        self.ejecutando = ejecutando
        self.estado_juego = estado_juego
        
    
    def actualizar(self, eventos):
        self.eventos = eventos
        for evento in self.eventos:
            
            if evento.type == pygame.QUIT:
                self.ejecutando = False
            
            if evento.type == pygame.KEYDOWN:
                
                if self.estado_juego.estado == 'menu':
                    if evento.key == pygame.K_ESCAPE:
                        self.ejecutando = False
                        
                elif self.estado_juego.estado == 'juego':
                    if evento.key ==pygame.K_ESCAPE:
                        self.estado_juego.estado = 'pausa'
                    
                    if evento.key == pygame.K_SPACE:
                        self.estado_juego.Disparar()
                
                elif self.estado_juego.estado == 'pausa':
                    
                    if evento.key == pygame.K_ESCAPE:
                        self.estado_juego.estado = 'juego'

                    if evento.key == pygame.K_r:
                        self.estado_juego.inicializar()
                        self.estado_juego.estado = 'juego'
                    
                    if evento.key == pygame.K_m:
                        self.estado_juego.inicializar()
                        self.estado_juego.estado = 'menu'
                        
                elif self.estado_juego.estado == 'game_over':
                    
                    if evento.key == pygame.K_r:
                        self.estado_juego.inicializar()
                        self.estado_juego.estado ='juego'
                    
                    if evento.key == pygame.K_m:
                        self.estado_juego.inicializar()
                        self.estado_juego.estado = 'menu'
               
        return self.ejecutando