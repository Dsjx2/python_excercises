class Orden:
    contador_ordenes = 0

    def __init__(self):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = []

    @property
    def id_orden(self):
        return self._id_orden

    @property
    def computadoras(self):
        return self._computadoras

    def agregar_computadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        str_computadora = ""
        for  computadora in self._computadoras:
            str_computadora += f" {computadora}"
        return f'''
        Orden: {self._id_orden}
Computadoras: 
{str_computadora}
'''