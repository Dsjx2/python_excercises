class Pelicula:
    contador_pelicula = 0
    def __init__(self, nombre):
        self.nombre = nombre
        self.pelicula_id = Pelicula.contador_pelicula
        Pelicula.contador_pelicula += 1

    def mostrar_pelicula(self):
        return f'Pelicula -> {self.nombre}'

    def __str__(self):
        return f'{self.nombre}'

    def escribir_pelicula(self):
        return f'{self.pelicula_id},{self.nombre}'

    @classmethod
    def reset_contador(cls,contador):
        cls.contador_pelicula = contador