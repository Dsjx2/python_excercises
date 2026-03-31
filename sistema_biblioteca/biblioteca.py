from libro import Libro

class Biblioteca:
    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []

    def agregar_libros(self, libro):
        self._libros.append(libro)

    def buscar_libros_autor(self, autor):
        for libro in self._libros:
            if libro.autor.lower() == autor.lower():
                self.mostrar_libro(libro)

    def buscar_libros_genero(self, genero):
        for libro in self._libros:
            if libro.genero.lower() == genero.lower():
                self.mostrar_libro(libro)

    def buscar_libro(self, titulo):
        for libro in self._libros:
            if libro.titulo.lower() == titulo.lower():
                self.mostrar_libro(libro)

    def mostrar_todos_libros(self):
        print(f'Todos los libros de la biblioteca {self._nombre}')
        for libro in self._libros:
            self.mostrar_libro(libro)

    def mostrar_libro(self,libro:Libro):
        print(libro)

    @property
    def nombre(self):
        return self._nombre

    @property
    def libros(self):
        return self._libros