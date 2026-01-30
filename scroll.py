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
colores_vivos = ["cyan", "green", "yellow", "bright_magenta", "orange1", "spring_green3"]

def imprimir_frase_animada(texto):
    color = random.choice(colores_vivos)
    frase = f">> {texto} <<"
    
    # TRUCO: Subimos el cursor 2 líneas para escribir sobre el hueco que dejamos
    # \033[F sube una línea, \033[K limpia la línea actual
    sys.stdout.write("\033[F" * 2) 
    
    for i in range(len(frase) + 1):
        sys.stdout.write("\r\033[K") # Regresa al inicio y limpia la línea
        console.print(f"[{color}]{frase[:i]}[/{color}]", end="")
        sys.stdout.flush()
        time.sleep(0.05)
    
    # Bajamos el cursor de nuevo para que el programa siga su flujo normal
    print("\n") 

# --- BUCLE PRINCIPAL ---
indice_anterior = -1
os.system("cls" if os.name == "nt" else "clear")

try:
    while True:
        tiempo_actual = (time.time() - tiempo_inicio) + tiempo_offset
        
        indice_actual = 0
        for i, elemento in enumerate(letra):
            if tiempo_actual >= elemento["tiempo"]:
                indice_actual = i
            else:
                break

        if indice_actual != indice_anterior:
            os.system("cls" if os.name == "nt" else "clear")
            
            # 1. Header
            console.print(f"[bold white on blue]  KARAOKE MODE  [/bold white on blue] [yellow] {tiempo_actual:.2f}s[/yellow]\n")
            
            # 2. Línea anterior (Gris)
            if indice_actual > 0:
                console.print(f"[grey37]   {letra[indice_actual - 1]['texto']}[/grey37]")
            else:
                print("")

            # 3. HUECO PARA LA LÍNEA ACTUAL (Lo dejamos vacío pero reservamos el espacio)
            print("") 

            # 4. Línea siguiente (Gris - APARECE DE INMEDIATO)
            if indice_actual < len(letra) - 1:
                console.print(f"[grey37]   {letra[indice_actual + 1]['texto']}[/grey37]")
            else:
                print("")

            # 5. DISPARAMOS EL EFECTO (Subirá el cursor para rellenar el hueco)
            imprimir_frase_animada(letra[indice_actual]['texto'])
            
            indice_anterior = indice_actual

        time.sleep(0.01)
except KeyboardInterrupt:
    pygame.mixer.music.stop()