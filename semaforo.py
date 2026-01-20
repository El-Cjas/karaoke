import os
import time
os.system('color')


COLORES = {
    "ROJO": "\033[1;31m",
    "VERDE": "\033[1;32m",
    "AMARILLO": "\033[33m",
    "RESET": "\033[0m"
}
señales = ["ALTO 🛑", "AVANCE ✅", "PRECAUCIÓN ⚠"]

configuracion = [
    (COLORES["ROJO"],"ALTO 🛑",3),
    (COLORES["VERDE"],"AVANCE ✅",3),
    (COLORES["AMARILLO"],"PRECAUCIÓN ⚠",1)
]




try:
    while True:
        for color, señal ,espera in configuracion:
            os.system("cls")
            print( color + señal + COLORES["RESET"])
            time.sleep(espera)
except KeyboardInterrupt:
    print("\033[34m programa finalizado \033[0m")
# semaforo = dict(zip(COLORES.values(), señales))