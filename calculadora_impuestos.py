print("***Calculadora de impuestos***")


def calcular_impuestos(monto:float, impuesto:float)->float:
    pago_total =  monto + monto * (impuesto/100)
    print(f'Pago con impuesto: {pago_total}')

monto = float(input('Ingresa el monto de pago sin impuesto: '))
impuesto = float(input('Ingresa el monto del impuesto: '))

calcular_impuestos(monto,impuesto)




