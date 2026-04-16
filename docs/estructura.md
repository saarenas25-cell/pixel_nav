#  Estructura del Proyecto - Pixel Nav 

Este documento describe la organización de carpetas y archivos del proyecto, así como la función de cada uno dentro del desarrollo del videojuego.

---

##  Estructura general

```
pixel_nav/
├── src/
├── assets/
├── data/
├── docs/
├── README.md
├── requirements.txt
```

---

##  src/

Contiene todo el código fuente del videojuego. Aquí se encuentra la lógica principal, las clases y funciones que controlan el comportamiento del juego.

**Archivos principales:**

* `main.py`: Punto de entrada del juego. Inicializa Pygame y ejecuta el bucle principal.
* `nave.py`: Contiene la clase de la nave del jugador y su comportamiento.
* `enemigos.py`: Maneja la lógica y comportamiento de los enemigos.
* `utilidades.py`: Librería propia del proyecto con funciones reutilizables (cálculos, lógica auxiliar, etc.).

---

##  assets/

Contiene todos los recursos visuales y auditivos utilizados en el juego.

**Subcarpetas:**

* `imagenes/`: Sprites, fondos y gráficos del juego.
* `sonidos/`: Efectos de sonido y música.

---

##  data/

Almacena datos del juego que pueden cambiar durante la ejecución.

**Ejemplos:**

* Puntajes del jugador
* Configuraciones
* Estados guardados

---

##  docs/

Contiene la documentación del proyecto en formato Markdown.

**Archivos:**

* `documentacion.md`: Documento principal del proyecto (explicación general, historia, funcionamiento).
* `estructura.md`: Descripción de la estructura del proyecto.

---

##  README.md

Archivo principal de presentación del proyecto. Incluye una descripción general, instrucciones de uso y ejecución.

---

##  requirements.txt

Lista de dependencias necesarias para ejecutar el proyecto.

**Ejemplo:**

```
pygame
```

---

##  Notas adicionales

* El proyecto está organizado de manera modular para facilitar su mantenimiento y escalabilidad.
* Se separa la lógica del juego de los recursos gráficos para una mejor estructura.
* Se implementa una librería propia (`utilidades.py`) para cumplir con los requisitos del proyecto.

---
