import pygame, time, os
from parsear import parsear_lrc
from rich import print

pygame.mixer.init()
pygame.mixer.music.load(r"canciones\Ozuna Ft. J Balvin, Chencho Corleone - Una Locura.mp3")
pygame.mixer.music.play()

delay = 1.2
letra = parsear_lrc(r"letras\Ozuna - Una Locura.es.lrc")

# Variables de control de tiempo
tiempo_offset = 0  # Cuántos segundos hemos adelantado/atrasado manualmente
tiempo_inicio = time.time()
indice_letra = 0

def obtener_tiempo_actual():
    # El tiempo real es: tiempo transcurrido desde el inicio + saltos manuales
    return (time.time() - tiempo_inicio) + tiempo_offset

os.system("cls")

# BUCLE PRINCIPAL
running = True
while running:
    # 1. CALCULAR TIEMPO ACTUAL
    tiempo_actual = obtener_tiempo_actual()
    
    # 2. LÓGICA DE ADELANTAR (Simulado con input o evento)
    # En un juego real usarías pygame.event.get()
    # Aquí un ejemplo lógico: si presionas una tecla, haces esto:
    """
    if tecla_derecha_presionada:
        salto = 10
        tiempo_offset += salto
        # Importante: sincronizar el mp3
        pygame.mixer.music.play(start=tiempo_actual + salto) 
    """

    # 3. BUSCAR LA LETRA CORRECTA (Sincronización dinámica)
    # Buscamos la frase que corresponde al tiempo actual
    frase_actual = ""
    for elemento in letra:
        if tiempo_actual >= (elemento["tiempo"] - delay):
            frase_actual = elemento["texto"]
        else:
            break # Como la letra está ordenada, dejamos de buscar

    # 4. RENDERIZADO (Solo limpiar si la letra cambia para evitar parpadeo)
    os.system("cls")
    print(f"Tiempo: {tiempo_actual:.2f}")
    print(f"\n[bold magenta]{frase_actual}[/bold magenta]\n")
    
    time.sleep(0.05) # Pequeña pausa para no saturar el CPU