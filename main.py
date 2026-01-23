import pygame, time, os
from parsear import parsear_lrc
from rich import print 
pygame.mixer.init()
pygame.mixer.music.load("canciones\Maluma - Hawái (Official Video) - MalumaVEVO.mp3")
pygame.mixer.music.play()

#configurar delay de la cancion, en caso de no tener delay entra la letra y el tiempo de la cancion pues dejarlo en cero
delay = 0
tiempo_inicio = time.time()
tiempo_offset = 0  # Cuántos segundos hemos adelantado/atrasado manualmente


letra = parsear_lrc("letras\Maluma-Hawai-(Official-Video) (1).lrc")
parte = letra[0]
##print(parte.values())
num_elementos = len(letra)

os.system("cls")

def obtener_tiempo_actual():
    # El tiempo real es: tiempo transcurrido desde el inicio + saltos manuales
    return (time.time() - tiempo_inicio) + tiempo_offset

running = True
while running:
    for elemento in letra:
        while (time.time() - tiempo_inicio) < elemento["tiempo"] - delay:
            time.sleep(0.1)
        os.system("cls")
        # print(pygame.mixer.music.get_pos())
        print(elemento["texto"])

