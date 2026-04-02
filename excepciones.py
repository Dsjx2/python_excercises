def division(numerador, denominador):
    try:
        if denominador == 0:
            raise ZeroDivisionError('El denominador no puede ser 0')

        result = numerador/denominador
        print(result)
    except ZeroDivisionError as e:
        print(f'error: {e}')
    else:
        print('no ocurrio ningun error')
    finally:
        print('excepcion finalizada')


division(3,0)
division(4,2)
division(45,'')

