# Sistema de empleados

print("Datos del empleado")
nombre_empleado = input("Nombre: ")
edad_empleado = int(input("Edad: "))
salario_empleado = float(input("Salario: "))
jefe_dpto = input("Es Jefe: (Si/NO) ")

es_jefe_dpto = jefe_dpto.lower() == "si"

print('Datos del empleado')
print(f'Nombre: {nombre_empleado}')
print(f'Edad: {edad_empleado}')
print(f'Salario: {salario_empleado:.2f}')
print(f'Es jefe de depto: {es_jefe_dpto}')