import tkinter as tk
from pathlib import Path

from funciones_qtile import reiniciar_qtile
from funciones_sistema import run_comandos

def accion_boton1():
    etiqueta_resultado.config(text="DRACULA")
    path.write_text(f"{contents}DRACULA")
    reiniciar_qtile()
    run_comandos(wallpaper='1')

def accion_boton2():
    etiqueta_resultado.config(text="NORD")
    path.write_text(f"{contents}NORD")
    reiniciar_qtile()
    run_comandos(wallpaper='2')

def accion_boton3():
    etiqueta_resultado.config(text="SOLARIZED_DARK")
    path.write_text(f"{contents}SOLARIZED_DARK")
    reiniciar_qtile()
    run_comandos(wallpaper='3')

def accion_boton4():
    etiqueta_resultado.config(text="CUSTOM")
    path.write_text(f"{contents}CUSTOM")
    reiniciar_qtile()
    run_comandos(wallpaper='4')

# Ruta de los colores
path = Path('../.config/qtile/current_theme.py')
contents = ("from theme.colors import Colors\n"
            "colors = Colors.")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Interfaz con 4 Botones")
ventana.geometry("400x300")

# Marco para organizar los botones
marco_botones = tk.Frame(ventana)
marco_botones.pack(pady=20)

# Crear botones
boton1 = tk.Button(marco_botones, text="DRACULA", command=accion_boton1, bg="red", fg="white")
boton1.grid(row=0, column=0, padx=10, pady=5)

boton2 = tk.Button(marco_botones, text="NORD", command=accion_boton2, bg="green", fg="white")
boton2.grid(row=0, column=1, padx=10, pady=5)

boton3 = tk.Button(marco_botones, text="SOLARIZED_DARK", command=accion_boton3, bg="blue", fg="white")
boton3.grid(row=1, column=0, padx=10, pady=5)

boton4 = tk.Button(marco_botones, text="CUSTOM", command=accion_boton4, bg="purple", fg="white")
boton4.grid(row=1, column=1, padx=10, pady=5)

# Etiqueta para mostrar resultados
etiqueta_resultado = tk.Label(ventana, text="Presiona un botón...", font=("Arial", 12))
etiqueta_resultado.pack(pady=20)

# Ejecutar la aplicación
ventana.mainloop()