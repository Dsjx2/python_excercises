# Validacion de password
contra = False


while contra == False:
    contrasena = input("Ingrese su contrasena: ")
    contra = contrasena if len(contrasena) > 5 else False
else:
    print('Password Valido')