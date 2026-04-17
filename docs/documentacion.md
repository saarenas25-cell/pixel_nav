# Documentación del Proyecto - Pixel Nav

---

## 1. Introducción

Pixel Nav es un videojuego desarrollado en Python utilizando la librería Pygame. El proyecto tiene como objetivo aplicar conceptos fundamentales de programación mediante la creación de un sistema interactivo que combina lógica y representación gráfica.

El desarrollo del juego permite integrar estructuras de control, programación orientada a objetos y organización modular del código.

---

## 2. Objetivos

### Objetivo general

Desarrollar un videojuego funcional que integre lógica de programación y elementos gráficos utilizando Python.

### Objetivos específicos

- Implementar el movimiento del jugador
- Crear un sistema de disparo
- Desarrollar enemigos con comportamiento básico
- Implementar detección de colisiones
- Diseñar una interfaz gráfica funcional
- Aplicar una estructura modular del código
- Crear una librería propia reutilizable

---

## 3. Descripción del juego

El jugador controla una nave ubicada en la parte inferior de la pantalla que puede desplazarse horizontalmente (izquierda y derecha).

El objetivo es destruir enemigos que descienden desde la parte superior de la pantalla, evitando colisiones y acumulando puntos.

El juego incluye:
- Movimiento lateral del jugador
- Disparo de proyectiles
- Enemigos descendentes
- Sistema de puntaje
- Posibles mejoras (power-ups)
- Generación de elementos de forma dinámica

---

## 4. Lógica del sistema

El juego funciona mediante un ciclo principal (game loop) que se ejecuta constantemente mientras el juego está activo.

Este ciclo se divide en tres partes principales:

1. Captura de eventos  
   Se detectan acciones del usuario como pulsaciones de teclas o cierre de la ventana.

2. Actualización de la lógica  
   Se procesan los movimientos del jugador, enemigos, disparos y colisiones.

3. Renderizado  
   Se dibujan todos los elementos en pantalla.

Además, se controla la tasa de actualización (FPS) para mantener un rendimiento estable.

---

## 5. Clases principales

### Jugador

Representa la nave controlada por el usuario.

Responsabilidades:
- Manejar el movimiento horizontal
- Controlar los límites de pantalla
- Renderizarse en pantalla

---

## 6. Uso de estructuras de programación

El proyecto utiliza diversas estructuras fundamentales de programación:

- Condicionales  
  Para control de eventos, límites de pantalla y colisiones.

- Ciclos  
  Para el funcionamiento continuo del juego mediante el game loop.

- Clases  
  Para estructurar el código mediante programación orientada a objetos.

---

## 7. Librería propia

El proyecto incluye una librería propia ubicada en la carpeta `utilidades`.

Esta librería contiene funciones auxiliares reutilizables, como:

- 

---

## 8. Interfaz gráfica

El juego incluirae diferentes elementos de interfaz que permiten la interacción con el usuario:

- Menú principal
- Menú de pausa
- HUD (información en pantalla como puntaje o estado del jugador)
- Pantalla de fin de juego

Estos elementos permiten una experiencia de usuario más completa.

---

## 9. Trabajo en equipo

El desarrollo del proyecto se divide en dos áreas principales:

- Lógica del juego (movimiento, enemigos, colisiones)
- Interfaz y control del sistema (menús, estados, visualización)

Esta división permite un trabajo organizado y paralelo entre los integrantes del equipo.

---

## 10. Conclusión

El proyecto Pixel Nav permite aplicar conocimientos fundamentales de programación en un entorno práctico, integrando lógica, estructura y diseño interactivo.

Además, fomenta el trabajo en equipo y el uso de buenas prácticas en el desarrollo de software, cumpliendo con los requisitos establecidos para el proyecto académico.

---