from dispositivo_entrada import Dispositivo_Entrada

class Teclado(Dispositivo_Entrada):
    contador_teclados = 0

    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self.id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'Teclado -> Id: {self.id_teclado}, Marca: {self.marca}, Tipo de Entrada: {self.tipo_entrada}'

