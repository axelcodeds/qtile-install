from utilidades.funciones_sistema import copiar_carpeta
from instalacion.instalar_paquetes import instalar_paquetes
from instalacion.paquetes import paquetes

for clave, valor in paquetes.items():
    print(f"\n{'-'*20}Instalando {clave}{'-'*20}:\n")
    instalar_paquetes(valor)

origen = '../.config/qtile'
destino = '../.config/qtile-backup'

copiar_carpeta(origen, destino)