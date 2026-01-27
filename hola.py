import pygame, time, os
from parsear import parsear_lrc
from rich import print 

pygame.mixer.init()
pygame.mixer.music.load("canciones\Ana Gabriel   El Cigarrillo Letra - javier hernan panta seminario.mp3")
pygame.mixer.music.play()

delay = 0
tiempo_inicio = time.time()
tiempo_offset = 20 # Cuántos segundos hemos adelantado/atrasado manualmente
pygame.mixer.music.set_pos(tiempo_offset)

letra = parsear_lrc("letras/ana gabriel - el cigarrillo.lrc")

# --- VARIABLES DE CONTROL ---
indice_anterior = -1 
os.system("cls")

def obtener_tiempo_actual():
    return (time.time() - tiempo_inicio) + tiempo_offset

running = True
while running:
    tiempo_actual = obtener_tiempo_actual()
    
    # 1. ENCONTRAR EL ÍNDICE DE LA FRASE ACTUAL
    indice_actual = 0
    for i, elemento in enumerate(letra):
        if tiempo_actual >= (elemento["tiempo"] - delay):
            indice_actual = i
        else:
            break

    # 2. SOLO ACTUALIZAR SI EL ÍNDICE CAMBIÓ
    if indice_actual != indice_anterior:
        os.system("cls")
        print(f"[yellow]Tiempo: {tiempo_actual:.2f}[/yellow]\n")
        print("-" * 30)

        # --- MOSTRAR BLOQUE DE 3 LÍNEAS (Scroll) ---
        
        # Línea Anterior (si existe)
        if indice_actual > 0:
            print(f"[grey37]{letra[indice_actual - 1]['texto']}[/grey37]")
        else:
            print("") # Espacio vacío si es la primera

        # Línea Actual (Destacada)
        print(f"[bold magenta]> {letra[indice_actual]['texto']} <[/bold magenta]")

        # Línea Siguiente (si existe)
        if indice_actual < len(letra) - 1:
            print(f"[grey37]{letra[indice_actual + 1]['texto']}[/grey37]")
        
        print("-" * 30)
        
        indice_anterior = indice_actual

    time.sleep(0.05)