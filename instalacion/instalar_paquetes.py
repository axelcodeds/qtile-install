import subprocess
import sys

def instalar_paquetes(lista_paquetes, actualizar_primeros=False):
    """
    Instala paquetes en Arch Linux usando pacman.
    
    Args:
        lista_paquetes (list/tuple): Iterable con nombres de paquetes a instalar
        actualizar_primeros (bool): Si True, actualiza el sistema antes de instalar
    """
    if not lista_paquetes:
        print("No hay paquetes para instalar.")
        return
    
    try:
        # Actualizar el sistema primero si se especificó
        if actualizar_primeros:
            print("Actualizando el sistema...")
            subprocess.run(["sudo", "pacman", "-Syu", "--noconfirm"], check=True)
        
        # Instalar los paquetes
        print(f"Instalando paquetes: {', '.join(lista_paquetes)}")
        comando = ["sudo", "pacman", "-S", "--noconfirm", "--needed"] + lista_paquetes
        subprocess.run(comando, check=True)
        
        print("Instalación completada exitosamente!")
    
    except subprocess.CalledProcessError as e:
        print(f"Error durante la instalación: {e}", file=sys.stderr)
        sys.exit(1)
