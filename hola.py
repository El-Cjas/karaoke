import pygame, time, os, sys, random
from parsear import parsear_lrc
from rich.console import Console

console = Console()

# --- CONFIGURACIÓN ---
pygame.mixer.init()
pygame.mixer.music.load("canciones/Ana Gabriel - El Cigarrillo.mp3")
pygame.mixer.music.play()

tiempo_offset = 20 
pygame.mixer.music.set_pos(tiempo_offset)
tiempo_inicio = time.time()

letra = parsear_lrc("letras/ana gabriel - el cigarrillo.lrc")
colores_vivos = ["cyan", "bright_yellow", "bright_magenta", "spring_green3", "turquoise2"]

def imprimir_centrado_con_efecto(texto):
    """Limpia y muestra solo la frase actual con efecto de escritura"""
    color = random.choice(colores_vivos)
    os.system("cls" if os.name == "nt" else "clear")
    
    # Añadimos un poco de espacio superior para centrar verticalmente
    print("\n" * 1)
    
    frase_completa = f"{texto}"
    
    # Efecto de máquina de escribir
    for i in range(len(frase_completa) + 1):
        # Regresar al inicio de la línea para actualizar la palabra
        sys.stdout.write("\r")
        # Generar espacios para centrar horizontalmente (ajuste según ancho consola)
        padding = " " * 10 
        console.print(f"{padding}[bold {color}]{frase_completa[:i]}[/bold {color}]", end="")
        sys.stdout.flush()
        time.sleep(0.06)
    print("\n" * 2)

# --- BUCLE PRINCIPAL ---
indice_anterior = -1

try:
    while True:
        # Sincronización del tiempo
        tiempo_actual = (time.time() - tiempo_inicio) + tiempo_offset
        
        indice_actual = 0
        for i, elemento in enumerate(letra):
            if tiempo_actual >= elemento["tiempo"]:
                indice_actual = i
            else:
                break

        # Solo disparamos la función cuando cambia el verso
        if indice_actual != indice_anterior:
            imprimir_centrado_con_efecto(letra[indice_actual]['texto'])
            indice_anterior = indice_actual

        time.sleep(0.01)

except KeyboardInterrupt:
    pygame.mixer.music.stop()
    print("\n[bold red]Karaoke interrumpido.[/bold red]")