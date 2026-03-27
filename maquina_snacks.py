print('Bienvenido a la maquina de snacks')

snacks = []

class Snack:
    def __init__(self,id:int,nombre:str,precio:float):
        self.id = id
        self.nombre = nombre
        self.precio = precio

snack1 = Snack(1,'Cheetos',2.0).__dict__
snack2 = Snack(2,'Crujitos',3.0).__dict__
snack3 = Snack(3,'Nachos',4.0).__dict__
snack4 = Snack(4,'Palitos',0.5).__dict__
snack5 = Snack(5,'Elotitos',0.5).__dict__

snacks.append(snack1)
snacks.append(snack2)
snacks.append(snack3)
snacks.append(snack4)
snacks.append(snack5)

def GetSnack(id:int):
    for snack in snacks:
        if snack['id'] == id:
            return snack

carrito = []

carrito_ok = False

def MostrarProductos(snacks):
    for item in snacks:
        print(f'{item['id']},{item["nombre"]},{item["precio"]}')

def MostrarMenu():
    print('1. Mostrar Snacks')
    print('2. Comprar Snacks')
    print('3. Mostrar ticket')
    print('4. Salir')

MostrarMenu()
while not carrito_ok:
    option = int(input('Ingresa la opcion: '))
    if option == 1:
        MostrarProductos(snacks)
    elif option == 2:
        select = int(input('Ingresa el id del snack : '))
        carrito.append(GetSnack(select))
        print(f'Snack agregado {GetSnack(select)['nombre']}: Precio: Q. {GetSnack(select)['precio']}')
    elif option ==3:
        total_carrito = 0
        for item in carrito:
            total_carrito += item['precio']
        print('=======Total del ticket: ==========')
        MostrarProductos(carrito)
        print(f'Total: Q. {total_carrito}')
    elif option ==4:
        print('Muchas gracias por utilizar el servicio')
        carrito_ok = True
    else:
        print('Opcion Invalida, por favor selecciona otra opcion')

