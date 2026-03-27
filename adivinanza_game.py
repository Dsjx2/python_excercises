# Juego de adivinanzas
import random

print('Juego de adivinanzas')

numero_secreto = random.randint(1, 50)

intentos = 0
ok = False
print(numero_secreto)
while (ok == False):
    intentos += 1
    tu_numero = int(input('Ingrese un numero entre 1 y 50: '))
    if (numero_secreto == tu_numero):
        ok = True
    else:
        result = 'Mayor' if numero_secreto > int(tu_numero) else 'Menor'
        print(result ,' Intento No.', intentos)

print('Lo adivinaste en' ,intentos, ' intentos')

