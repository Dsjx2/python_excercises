class Snack:
    contador_snacks = 0
    def __init__(self, nombre='', precio=0.0):
        Snack.contador_snacks += 1
        self.nombre = nombre
        self._precio = precio
        self._id_snack = Snack.contador_snacks

    @property
    def id_snack(self):
        return self._id_snack

    @property
    def precio(self):
        return self._precio


    def __str__(self):
        return f'Snack -> {self._id_snack} -> : Nombre-> {self.nombre} : Precio-> {self._precio}'

    def escribir_snack(self):
        return f'{self._id_snack},{self.nombre},{self._precio}'