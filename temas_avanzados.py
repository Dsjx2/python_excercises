# comprension de listas
from functools import reduce

lista = [f'Numero: {x}' for x in range(0, 20) if x % 2 == 0]

# for i in lista:
#     print(i)

# Funcion Zip
nombre = ['Juan', 'Maria', 'Pedro']
edad = [23, 66, 43]
ciudades = ['Guatemala', 'El Salvador', 'EEUU']

personas = zip(nombre, edad, ciudades)

# for persona in personas:
#     print(persona)

# Funcion Split

cadena = 'Hola mundo'
palabras = cadena.split(' ')

# for p in palabras:
#     print(p)

# Funcion Buscar y reemplazar

posicion = cadena.find('mundo')

# print(f'Posicion de la cadena mundo: {posicion}')

nueva_cadena = cadena.replace('mundo', 'Amigo')
# print(f'Nueva cadena reemplazada: {nueva_cadena}')

# Multiplicacion de cadenas

cadena = 'Hola '
resultado_multiplicacion_cadenas = cadena * 5
# print(f'resultado_multiplicacion_cadenas: {resultado_multiplicacion_cadenas}')


# Strip / limpiar una cadena

cadena = '        ..   Hola Mundo         .   .    '


# print(cadena)
# cadena_limpia = cadena.strip(' . ')
# print(cadena_limpia)


# Funciones lambda

# sin lambda
def cuadrado(x):
    return x ** 2


# print(f'Cuadrado del numero {cuadrado(4)}')

# con lambda
cuadradol = lambda x: x ** 2
# print(f'Cuadrado del numero 5 {cuadradol(4)}')

# Funcion map y lambda

numeros = [2, 5, 1, 47, 3, 2]
# Funcion lambda para obtener el cuadrado de cada numero
cuadrados = list(map(lambda x: x ** 2, numeros))

concatenado = list(map(lambda x: f'numero: {x}', numeros))
# for c in concatenado:
#     print(c)

# Function filter y lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))
# print(f'resultado usando filter: {pares}')

# Funcion reduce() y map

suma_acumulativa = reduce(lambda x, y: x + y, numeros)
# print(suma_acumulativa)

# Funcion sorted()
lista_ordenada = sorted(numeros)
lista_mixta = ['hola', 3, 'mundo', 2, '4', 32, 34, '12']
lista_int = list(filter(lambda x: type(x) == int, lista_mixta))
lista_str = list(filter(lambda x: type(x) == str, lista_mixta))

# print(sorted(lista_int))
# print(sorted(lista_str))

# sorted en un diccionario

empleados_dict = [
    {'nombre': 'Juan', 'salario': 2300},
    {'nombre': 'Pedro', 'salario': 4300},
    {'nombre': 'Maria', 'salario': 5300},
]

empleados_ordenados = sorted(empleados_dict, key=lambda x: x['nombre'])


# print('empleados ordenados: ',empleados_ordenados)

# Generadores en Python yield

def generador(maximo):
    contador = 0
    while contador < maximo:
        yield contador
        contador += 1


# Creamos un generador
var_generador = generador(10)

# Iteramos sobre el generador
for v in var_generador:
    # print(v)
    pass


# Expresiones generadores

generador = (x ** 2 for x in range(10) if x % 2 == 0)

# for g in generador:
#     print(g)

# Decoradores

def decorador_con_mensaje(mensaje):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            print(mensaje)
            return funcion(*args, **kwargs)

        return wrapper
    return decorador

@decorador_con_mensaje("iniciando")
def saludar(nombre):
    return f"Hola {nombre}"


# print(saludar('juan'))

# next sum

lista = [2,3,4,5]

iterador = iter(lista)

result = sum(lista)

elemento = next(iterador)

print(elemento)
