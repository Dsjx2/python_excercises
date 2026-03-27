# Sistema de tienda online

nombre = "Python"

detalle_producto = {
    'nombre': 'Bag',
    'precio': 23.5,
    'cantidad': 122,
    'disponible': True
}

for i, v in detalle_producto.items():
    print(f'{i} {v} el tipo almacenado es {type(v)}')

nombre = (nombre.center(26, "*"))

for i, n in enumerate(nombre):
    print(i, n)
