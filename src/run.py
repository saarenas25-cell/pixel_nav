import sys
import os

# ---------------------------------
# AGREGAR src AL PATH AUTOMÁTICAMENTE
# ---------------------------------
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# ---------------------------------
# EJECUTAR EL JUEGO
# ---------------------------------
from main import main

main()