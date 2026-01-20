import pygame, time
from parsear import parsear_lrc
from rich import print 
pygame.mixer.init()
pygame.mixer.music.load("canciones\Ozuna x J Balvin x Chencho Corleone - Una Locura (Video Oficial) - Ozuna.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_pos(114)



letra = parsear_lrc("letras\Ozuna - Una Locura.es.lrc")
parte = letra[0]
##print(parte.values())
num_elementos = len(letra)

lista = {'tiempo': 209.3, 'texto': 'by RentAnAdviser.com'}


for elemento in letra:
    print(elemento)
    for tiempo in elemento.values():
        print(tiempo)
        #print(f"minuto: {tiempo / 60}")