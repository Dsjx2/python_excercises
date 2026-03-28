print('*** Convertidor de temperatura ***')

def celsius_fahrenheit(celsius)->float:
    return celsius *9/5+32

def fahrenheit_celsius(fahrenheit)->float:
    return fahrenheit - 32*5/9

while True:
    print('''
    Seleccione el tipo de conversion
    
    1. Celsius a Fahrenheit
    2. Fahrenheit a Celsius
    3. Salir
    ''')
    option = int(input('Ingrese la opcion: '))

    if option == 1:
        valor = float(input('Ingrese el valor en Celsius: '))
        print(f'Resultado {celsius_fahrenheit(valor):.2f} grados Fahrenheit')
        break
    elif option == 2:
        valor = float(input('Ingrese el valor en Fahrenheit: '))
        print(f'Resultado {fahrenheit_celsius(valor):.2f} grados Celsius')
        break
    elif option == 3:
        print('Gracias por utilizar el app')
        break
    else:
        print('Opcion invalida')

