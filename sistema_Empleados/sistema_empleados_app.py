from sistema_Empleados.empresa import Empresa
from sistema_Empleados.empleado import Empleado
print('Sistema de empleados')

empresa1 = Empresa('dsTech')

#contratar algunos empleados

empresa1.contratar_empleado('Juan','Ventas')
empresa1.contratar_empleado('Pedro','Marketing')
empresa1.contratar_empleado('Ana','Ventas')
empresa1.contratar_empleado('Maria','Recursos Humanos')


#Obtener el total de objetos del tipo empleado


print(f'Total de empleados {Empleado.obtener_total_empleados()}')

# obtener no, de empleados por dpto:

print(f'Empleados en ventas: {empresa1.obtener_numero_empleados_departamento('Ventas')}')

#Mostrar a todos los empleados de la empresa
empresa1.obtener_total_empleados()