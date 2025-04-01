import shutil
import os
import subprocess

def run_comandos(wallpaper):
    """Ejecuta comandos mediante un arreglo en arxh linux"""
    commands = [
        f"feh --bg-fill ~/Pictures/wallpapers/blue/0{wallpaper}.jpg",
    ]
    
    for cmd in commands:
        try:
            # Usamos shell=True para manejar rutas con ~ y comandos complejos
            subprocess.Popen(cmd, shell=True)
        except Exception as e:
            print(f"Error al ejecutar '{cmd}': {e}")


def copiar_carpeta(origen, destino):
    """Copia una carpeta a otra."""
    if os.path.exists(destino):
        print(f"La carpeta {destino} ya existe.")
    else:
        try:
            shutil.copytree(origen, destino)
            print(f"Carpeta copiada de {origen} a {destino}")
        except Exception as e:
            print(f"Error al copiar la carpeta: {e}")