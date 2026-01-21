import time

inicio = time.time()

# Código que quieres medir
time.sleep(1.6) # Pausa de 1.5 segundos

fin = time.time()

print(f"El proceso tardó {fin - inicio} segundos")