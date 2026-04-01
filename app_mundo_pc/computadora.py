from monitor import Monitor
from teclado import Teclado
from raton import Raton


class Computadora:
    contador_computadora = 0

    def __init__(self, nombre, monitor:Monitor, teclado:Teclado, raton:Raton):
        Computadora.contador_computadora += 1
        self.id_computadora = Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return f"""Computadora: {self.id_computadora}
        {self.nombre}
        {self.monitor}
        {self.teclado}
        {self.raton}

"""