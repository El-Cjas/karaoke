import os
import time
os.system('color')

# Definición de colores
COLORES = {
    "ROJO": "\033[1;31m",
    "VERDE": "\033[1;32m",
    "AMARILLO": "\033[33m",
    "RESET": "\033[0m"
}
señales = ["ALTO 🛑", "AVANCE ✅", "AMARILLO ⚠"]

# semaforo = dict(zip(COLORES.values(), señales))

# Ejemplo de uso:

while True:
    for color, señal in zip(COLORES.values(), señales):
        os.system("cls")
        print( color + señal + COLORES["RESET"])
        time.sleep(2)


# while True:
#     os.system("cls")
#     print(COLORES["ROJO"] + "ALTO 🛑" + COLORES["RESET"])
#     time.sleep(2)
#     os.system("cls")
#     print(COLORES["VERDE"] + "PASE ✅" + COLORES["RESET"])
#     time.sleep(2)
#     os.system("cls")
#     print(COLORES["AMARILLO"] + "AMARILLO ⚠" + COLORES["RESET"])
#     time.sleep(2)
#     os.system("cls")
