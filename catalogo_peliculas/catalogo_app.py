from catalogo_peliculas.pelicula import Pelicula
from catalogo_peliculas.servicio_peliculas import ServicioPelicula


class CatalogoApp:
    def __init__(self):
        self.servicio_peliculas = ServicioPelicula()

    def mostrar_menu(self):
        print('''Seleccione la opcion deseada:
        1. Agregar Pelicula
        2. Listar Peliculas
        3. Eliminar Catalogo
        4. Salir
        ''')
        return int(input('Ingresa la opcion: '))

    def iniciar_catalogo(self):
        salir = False
        self.servicio_peliculas.listar_peliculas()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Error al ingresar la opcion: {e}')

    def ejecutar_opcion(self,opcion):
        if opcion == 1:
            self.agregar_pelicula()
        elif opcion == 2:
            self.servicio_peliculas.listar_peliculas()
        elif opcion == 3:
            self.servicio_peliculas.eliminar_pelicula()
            # Pelicula.reset_contador()
        elif opcion == 4:
            print('Gracias por utilizar nuestro servicio')
            return True
        else:
            print(f'Opcion no valida: {opcion}')

    def agregar_pelicula(self):
        nombre_pelicula = input('Ingrese el nombre de la pelicula:')
        nueva_pelicula = Pelicula(nombre_pelicula)
        self.servicio_peliculas.agregar_pelicula(nueva_pelicula)
        print(f'Pelicula {nombre_pelicula} agregado correctamente')

if __name__ == '__main__':
    app = CatalogoApp()
    app.iniciar_catalogo()
