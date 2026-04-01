from dispositivo_entrada import Dispositivo_Entrada

class Raton(Dispositivo_Entrada):
    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id_raton = Raton.contador_ratones
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'Raton -> Id: {self.id_raton}, Marca: {self.marca}, Tipo de Entrada: {self.tipo_entrada}'

