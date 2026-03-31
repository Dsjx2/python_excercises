class Animal:
    def hacer_sonido(self):
        print('Hago un pitido')

class Perro(Animal):
    def hacer_sonido(self):
        print("Puedo ladrar")

class Gato(Animal):
    def hacer_sonido(self):
        print("Puedo Maullar")

# Funcion polimorfica
def hacer_sonido_animal(animal):
    animal.hacer_sonido()


animal = Animal()
hacer_sonido_animal(animal)

perro = Perro()
hacer_sonido_animal(perro)

gato = Gato()
hacer_sonido_animal(gato)
