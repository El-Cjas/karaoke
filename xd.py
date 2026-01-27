from rich.console import Console
import os, time

console = Console(force_terminal=True)

# Simulamos la estructura que te devuelve tu función parsear_lrc
letra = [
    {"tiempo": 0, "texto": "--- INTRO ---"},
    {"tiempo": 2, "texto": "Ya yo me enteré, se nota cuando me ve'"},
    {"tiempo": 5, "texto": "Ahí donde esa' trabaja', hoy yo te voy a ver"},
    {"tiempo": 8, "texto": "Dime qué pasó, que todavía no has llega'o"},
    {"tiempo": 11, "texto": "Tú sabe' que yo te espero, no me dejes planta'o"},
    {"tiempo": 14, "texto": "--- CORO ---"},
]

def mostrar_pantalla(indice_actual, tiempo):
    os.system("cls" if os.name == "nt" else "clear")
    
    # Cabecera con estilo
    console.print("[grey37 italic]🎵 REPRODUCTOR V1.0[/grey37 italic]", justify="center")
    console.print(f"[italic white]Tiempo: {tiempo:.2f}s[/italic white]", justify="center")
    console.print("=" * 50, style="blue")

    # Scroll de 3 líneas con efectos distintos
    # 1. Anterior (itálica y opaca)
    if indice_actual > 0:
        console.print(f"   [grey37 italic]{letra[indice_actual - 1]['texto']}[/grey37 italic]", justify="left")
    else:
        console.print("")

    # 2. ACTUAL (El "Neon" reverse)
    # Usamos 'reverse' para que el fondo sea Cyan y la letra negra
    console.print(f" [reverse bold white on cyan]  ▶ {letra[indice_actual]['texto']}  [/reverse bold white on cyan]", justify="left")

    # 3. Siguiente (normal)
    if indice_actual < len(letra) - 1:
        console.print(f"   [grey50]{letra[indice_actual + 1]['texto']}[/grey50]", justify="left")
    
    console.print("=" * 50, style="blue")

# --- SIMULACIÓN RÁPIDA ---
for i in range(len(letra)):
    mostrar_pantalla(i, letra[i]["tiempo"])
    time.sleep(1.5) # Pausa para que puedas ver el efecto