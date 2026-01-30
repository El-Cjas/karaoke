import time
import sys
from colorama import init

# ESTO ES LO MÁS IMPORTANTE: Inicializa el soporte ANSI
init(autoreset=True)

print("Línea 1: Preparando motores...")
time.sleep(1)

# \033[1A sube una línea, \r vuelve al inicio
sys.stdout.write("\033[1A\r") 
# Limpiamos con espacios por si la línea nueva es más corta
sys.stdout.write("Línea 1: ¡Motores encendidos!          \n")

print("Línea 2: Despegando...")
time.sleep(1)