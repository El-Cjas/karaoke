import pygame, time, os
from parsear import parsear_lrc
from rich import print 
pygame.mixer.init()
pygame.mixer.music.load("canciones\Olvídala, Binomio De Oro De América, Video Letra - Sentir Vallenato - Sentir Vallenato.mp3")
pygame.mixer.music.play()

#configurar delay de la cancion, en caso de no tener delay entra la letra y el tiempo de la cancion pues dejarlo en cero
delay = 0
tiempo_offset = 20  # Cuántos segundos hemos adelantado/atrasado manualmente
tiempo_inicio = time.time()
pygame.mixer.music.set_pos(tiempo_offset)
indice_letra = 0


letra = parsear_lrc("letras\Binomio De Oro De America - Olvídala.lrc")
parte = letra[0]
##print(parte.values())
num_elementos = len(letra)

os.system("cls")

def obtener_tiempo_actual():
    # El tiempo real es: tiempo transcurrido desde el inicio + saltos manuales
    return (time.time() - tiempo_inicio) + tiempo_offset


# --- VARIABLES DE CONTROL ---
frase_anterior = ""  # Aquí guardaremos la frase que ya se imprimió
os.system("cls")
running = True
while running:
    # 1. CALCULAR TIEMPO ACTUAL
    tiempo_actual = obtener_tiempo_actual()

    frase_actual = ""
    for elemento in letra:
        if tiempo_actual >= (elemento["tiempo"] - delay):
            frase_actual = elemento["texto"]
        else:
            break  # Como la letra está ordenada, dejamos de buscar
    
    # 4. RENDERIZADO (Solo limpiar si la letra cambia para evitar parpadeo)
    
    

   # 2. LÓGICA DE ACTUALIZACIÓN (Solo si la frase cambió)
    if frase_actual != frase_anterior:
        os.system("cls")
        print(f"Tiempo: {tiempo_actual:.2f}")
        print(f"\n[bold magenta]{frase_actual}[/bold magenta]\n")
        
        # Actualizamos la frase anterior para que en la próxima vuelta sepa que ya la puso
        frase_anterior = frase_actual

    time.sleep(0.05)