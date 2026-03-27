print('Sistema de inventario')

inventario_ok = False
inventario = []

while inventario_ok == False:
    new = int(input('Ingresar un nuevo item? 1 para agregar/ 2 para cancelar'))
    item = {}
    if new == 1:
        item['item'] = input('Ingresar un nuevo item: ')
        item['cantidad'] = int(input('Ingresar la cantidad: '))
        item['precio'] = float(input('Ingresar el precio: '))

        inventario.append(item)
    else:
        inventario_ok = True

print('Lista de productos')

for i, item in enumerate(inventario):
    print(f'{i}, Producto: {item["item"]}, Cantidad: {item['cantidad']}, Precio: {item["precio"]:.2f}')
