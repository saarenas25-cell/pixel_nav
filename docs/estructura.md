*Este documento representa la estructura actual del proyecto y su planificación.*
*Algunas carpetas pueden estar en desarrollo o pendientes de implementación.*

#  Estructura del Proyecto - Pixel Nav 

Este documento describe la organización de carpetas y archivos del proyecto, así como la función de cada uno dentro del desarrollo del videojuego.

---

##  Estructura general

pixel_nav/
├── src/                    ## **codigo fuente**
|   ├──main.py
|   ├──players/
|   |  ├──__init__.py
|   |  ├──jugador.py
|   |  ├──hud.py
│   ├── proyectiles/
│   │   ├── __init__.py
│   │   ├── proyectil.py
│   │   ├── bala.py
|   ├──utilidades/
|      ├──__init__.py
|      ├──librerias_propias.py
├── assets/                 ##  **imagenes, sonido, fuesntes**
├── data/                   ##  **Almacena datos del juego**
├── docs/                   ##  **documentacion**
|   ├──documentacion.md
|   ├──estructura.md
├── ui/                     ##  **Menús, interfaz y HUD**
├── README.md               ##  **explicacion del prollecto**
├── requirements.txt        ##  **dependencias**


---

##  src/ 

Contiene todo el código fuente del videojuego. Aquí se encuentra la lógica principal, las clases y funciones que controlan el comportamiento del juego.

**Archivos principales:**

*main.py*: Punto de entrada del juego. Inicializa Pygame y ejecuta el bucle principal.
*players/*: pundo donde se encuntra el odjeto de renderisar el jugador.
    **__init__.py**:
    Permite que la carpeta 'players' sea tratada como un módulo de Python y facilita la importación de sus clases.
    **jugador.py**:
    Define la clase Jugador, incluyendo:
    - Movimiento
    - Renderizado
    - Límites de pantalla
    **hud.py**
    -energia
    -vida
    -cuadro de vida
    cuadro de energia
*utilidades/*: punto donde se encuentran las librerias propias
    **__init__.py**:
    Permite que la carpeta 'utilidades' sea tratada como un módulo de Python y facilita la importación de sus clases.
    **librerias_propia.py**:
    se encuntra reservado para las librerias propias requeridas por el prollecto

--

##  assets/ 

reservada Contiene todos los recursos visuales y auditivos utilizados en el juego.

---

##  data/ 

reservada para Almacena información del juego que puede cambiar durante la ejecución, como:
- Puntajes
- Configuraciones
- Progreso del jugador

---

##  docs/ 

Contiene la documentación del proyecto en formato .md

Incluye:

**documentacion.md** → Explicación completa del proyecto  
**estructura.md** → Organización del código  

---

##  ui/ 

reservada para los elementos de interfaz gráfica del juego, como:
- Menú principal
- Menú de pausa
- HUD (información en pantalla)

---

##  README.md 

Archivo principal de presentación del proyecto. Incluye:
- Descripción general
- Controles
- Instrucciones de ejecución

---

##  requirements.txt 

Lista de dependencias necesarias para ejecutar el proyecto, como la librería Pygame.

---
