from raton import Raton
from monitor import Monitor
from teclado import Teclado
from computadora import Computadora
from orden import Orden


monitor = Monitor('HP',17)
raton = Raton('Logitech', 'USB')
teclado = Teclado('redDragon', 'Bluetooth')

monitor2 = Monitor('HP',17)
raton2 = Raton('Logitech', 'USB')
teclado2 = Teclado('redDragon', 'Bluetooth')

monitor3 = Monitor('Asus',17)
raton3 = Raton('AirSis', 'USB')
teclado3 = Teclado('Teclast', 'Bluetooth')


computadora = Computadora('Gamer',monitor,teclado,raton)
computadora2 = Computadora('Armada', monitor2,teclado2,raton2)
computadora3 = Computadora('Dell', monitor3,teclado3,raton3)

orden = Orden()
orden.agregar_computadora(computadora)
orden.agregar_computadora(computadora2)
orden.agregar_computadora(computadora3)

print(orden)
