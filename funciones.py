print('Funciones')

def sumar(a,b):
    return a+b

# llamar a la funcion sumar
result =sumar(4,5)
print(result)

# Funcion para retornar varios valores
def obtenerCoordenadas():
    x, y, z = 23,543,6
    return x,y,z

x,y,z = obtenerCoordenadas()
print(x,y,z)

# argumentos variables *args (Valores como tupla)

def super_poderes(heroe, nombre, *args):
    print(f'{heroe}, {nombre}, {args}')

    #iteramos args
    for poder in args:
        print(f'\tSuperpoder: {poder}')

super_poderes('Spiderman', 'Peter parker','telarania','Instinto aracnido')

# keyword arguments **kwargs (Valores como un dict)

def super_heroe(nombre,*args, **kwargs):
    print(f'Superheroe: {nombre}, {args}, - Mas info: {kwargs}')
    print(f'{type(args)}, {type(kwargs)}')

super_heroe('Spiderman','Instinto Aracnido','Telarania',edad = 23, empresa = 'Marvel')


# Suma de args
def sumar(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sumar(10,10,10))

# Iteracion de **kwargs

def imprimir_dict(**kwargs):
    print('Valores recibidos')
    for key, value in kwargs.items():
        print(f'{key}: {value}')

value = {
    'name':'daniel',
    'age':32,
    'direccion':'san juan sac',
    'telefono':'43434343'
    }

imprimir_dict(**value)
