nombre_archivo = 'snacks.txt'

from snack import Snack
snacks = []
def cargar_snacks_iniciales():
    snacks_iniciales = [
        Snack('Papas', 77),
        Snack('Sabritas', 60),
        Snack('Nachos', 70),
        Snack('HotDog', 50),
        Snack('Sandwich', 75),
    ]
    snacks.extend(snacks_iniciales)
    guardar_snacks_archivo(snacks_iniciales)

def guardar_snacks_archivo(snacks):
    try:
        with open(nombre_archivo, 'a') as archivo:
            for snack in snacks:
                archivo.write(f'{snack.escribir_snack()}\n')
    except Exception as e:
        print(f'Error al guardar snacks en archivo: {e}')

cargar_snacks_iniciales()