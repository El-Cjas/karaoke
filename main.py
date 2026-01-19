import os
os.system('color') # Esta línea "despierta" los colores en la terminal de Windows


# Definimos los "pinceles"
ROJO = "\033[31m"
VERDE = "\033[32m"
AZUL = "\033[34m"
RESET = "\033[0m"

# Ahora los usamos de forma fácil
print(f"{ROJO}¡Cuidado! Algo salió mal.{RESET}, jajajajaja {AZUL} O no...")
print(f"{AZUL}Procesando datos...{RESET}")
print(f"{VERDE}¡Éxito total!{RESET}")