import pygame, time
from parsear import parsear_lrc
from rich import print 
pygame.mixer.init()
pygame.mixer.music.load("canciones\Ozuna x J Balvin x Chencho Corleone - Una Locura (Video Oficial) - Ozuna.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_pos(0)

tiempo_incio = time.time()


letra = parsear_lrc("letras\Ozuna - Una Locura.es.lrc")
parte = letra[0]
##print(parte.values())
num_elementos = len(letra)



for elemento in letra:
    
    while (time.time() - tiempo_incio) < elemento["tiempo"]:
        time.sleep(0.09)
    print(elemento["texto"])