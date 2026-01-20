import re

#esta funcion devuelve una lista con diccionarios en donde las claves "tiempo" y "texto"
def parsear_lrc(archivo_ruta):
    letras_sincronizadas = []
    
    # Expresión regular para capturar [minutos:segundos.centisegundos] Texto
    patron = re.compile(r'\[(\d+):(\d+\.\d+)\](.*)')

    try:
        with open(archivo_ruta, 'r', encoding='utf-8') as f:
            for linea in f:
                coincidencia = patron.match(linea.strip())
                if coincidencia:
                    minutos = int(coincidencia.group(1))
                    segundos = float(coincidencia.group(2))
                    texto = coincidencia.group(3).strip()
                    
                    # Convertir todo a segundos totales
                    tiempo_total = minutos * 60 + segundos
                    letras_sincronizadas.append({"tiempo": tiempo_total, "texto": texto})
    except FileNotFoundError:
        print("¡Error! No se encontró el archivo de letra.")
        
    return letras_sincronizadas

# Ejemplo de uso:
# letra = parsear_lrc("letras\Ozuna - Una Locura.es.lrc")
# for linea in letra:
#     print(f"En el segundo {linea['tiempo']}: {linea['texto']}")