print('*****Calculadora*****')


print('''
    OPERACIONES A REALIZAR
    
    1. SUMA
    2. RESTA
    3. MULTIPLICAR
    4. DIVIDIR
    5. SALIR
    
    ''')

def suma(num1,num2):
    return num1+num2
def resta(num1,num2):
    return num1-num2
def multiplicar(num1,num2):
    return num1*num2
def dividir(num1,num2):
    return num1/num2

def getNum():
    a = int(input("Ingresa el primer valor: "))
    b = int(input("Ingresa el segundo valor: "))
    return a,b

while True:
    try:
        option = int(input('Escoge una opcion: '))
    except ValueError:
        print("Debes ingresar un numero valido")
        continue
    if option == 1:
        a, b = getNum()
        result = suma(a,b)
        print('El resultado de la suma es : ', result)
    elif option == 2:
        a, b = getNum()
        result = resta(a, b)
        print('El resultado de la resta es: ', result)
    elif option == 3:
        a, b = getNum()
        result = multiplicar(a, b)
        print('El resultado dela multiplicacion es: ', result)
    elif option == 4:
        a, b = getNum()
        result = dividir(a, b)
        print('El resultado de la division es: ', result)
    elif option == 5:
        print('Gracias por utilizar esta app')
        break
    else:
        print('Opcion invalida')
