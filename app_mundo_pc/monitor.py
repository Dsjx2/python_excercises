class Monitor:
    contador_monitores = 0

    def __init__(self, marca, tamanio):
        Monitor.contador_monitores += 1
        self.marca = marca
        self.tamanio = tamanio
        self.id_monitor = Monitor.contador_monitores


    def __str__(self):
        return f'Monitor -> Id: {self.id_monitor}, Marca: {self.marca}, Tamanio: {self.tamanio}'