USER = 'admin'
PASS = '123'

usuario = input('Ingresa tu usuario')
password = input('Ingresa tu password')

datos_correctos = False

usuario_correcto = usuario if usuario == USER else False
pass_correcto = password if password == PASS else False

if (usuario_correcto and pass_correcto):
    datos_correctos = True

print(datos_correctos)