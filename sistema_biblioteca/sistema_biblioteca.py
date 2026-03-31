from biblioteca import Biblioteca
from libro import Libro

biblioteca1 = Biblioteca('Biblioteca Nacional')

Libro1 = Libro('El Señor Presidente', 'Miguel Ángel Asturias', 'Novela política')
Libro2 = Libro('Hombres de maíz', 'Miguel Ángel Asturias', 'Realismo mágico')
Libro3 = Libro('Cien años de soledad', 'Gabriel García Márquez', 'Realismo mágico')
Libro4 = Libro('La ciudad y los perros', 'Mario Vargas Llosa', 'Novela')
Libro5 = Libro('Rayuela', 'Julio Cortázar', 'Novela experimental')

biblioteca1.agregar_libros(Libro1)
biblioteca1.agregar_libros(Libro2)
biblioteca1.agregar_libros(Libro3)
biblioteca1.agregar_libros(Libro4)
biblioteca1.agregar_libros(Libro5)

# Mostrar todos los libros
biblioteca1.mostrar_todos_libros()

print("Mostrar solo del genero")
biblioteca1.buscar_libros_genero('Realismo mágico')

print("Mostrar solo del autor")
biblioteca1.buscar_libros_autor('Gabriel García Márquez')

print("Mostrar por titulo")
biblioteca1.buscar_libro('Rayuela')
