from pelicula import Pelicula
import os

class ServicioPelicula:
    NOMBRE_ARCHIVO = 'peliculas.txt'
    def __init__(self):
        self.catalogo = []
        if not os.path.isfile(ServicioPelicula.NOMBRE_ARCHIVO):
            self.catalogo = self.crear_catalogo()
        else:
            self.catalogo = self.cargar_catalogo()

    def crear_catalogo(self):
        catalogo_inicial = [
            Pelicula('Superman'),
            Pelicula('Spiderman'),
            Pelicula('Batman')
        ]
        self.catalogo.extend(catalogo_inicial)
        self.crear_archivo_catalogo(catalogo_inicial)

    def crear_archivo_catalogo(self, catalogo_inicial):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as file:
                for peli in catalogo_inicial:
                    file.write(f'{peli.escribir_pelicula()}\n')
        except Exception as e:
            print(f'Error: {e}')

    def cargar_catalogo(self):
        catalogo = []
        try:
            with open(self.NOMBRE_ARCHIVO) as file:
                for peli in file:
                    peli_id, peli_name = peli.split(',')
                    pelicula = Pelicula(peli_name)
                    catalogo.append(pelicula)
        except Exception as e:
            print(f'Error al leer el archivo: {e}')
        return catalogo

    def agregar_pelicula(self,nombre_pelicula):
        Pelicula.reset_contador(len(self.catalogo))
        self.catalogo.append(nombre_pelicula)
        self.crear_archivo_catalogo([nombre_pelicula])

    def listar_peliculas(self):
        print('Catalogo de Peliculas:')
        for peli in self.catalogo:
            print(f'{peli}'.strip())

    def eliminar_pelicula(self):
        try:
            if os.path.exists(ServicioPelicula.NOMBRE_ARCHIVO):
                os.remove(ServicioPelicula.NOMBRE_ARCHIVO)
                self.catalogo.clear()
                Pelicula.reset_contador(len(self.catalogo))
                print(f'Archivo {ServicioPelicula.NOMBRE_ARCHIVO} eliminado correctamente')
            else:
                print(f'El archivo {ServicioPelicula.NOMBRE_ARCHIVO} no existe')
        except Exception as e:
            print(f'Error: {e}')
