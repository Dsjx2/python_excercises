from random import randint

nombre = input("Ingrese su nombre: ")
nombre = nombre.strip().upper()[0:2]

apellido = input("Ingrese su apellido: ")
apellido = apellido.strip().upper()[0:2]

anio = str(2026)
anio = anio[2:4]

num_aleat = randint(1000,9999)

result = nombre + apellido + anio+''+str(num_aleat)
print(f'Tu numero de identificación es: {result}')