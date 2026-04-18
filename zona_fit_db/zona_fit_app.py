from zona_fit_db.cliente_dao import ClienteDAO
from zona_fit_db.cliente import Cliente

opcion = None

while opcion != 5:
    print('****  Clientes Zona Fit ***')
    print(f'''
        Menu
        1. Listar Clientes
        2. Agregar Clientes
        3. Modificar Cliente
        4. Eliminar
        5. Salir
        ''')

    opcion = int(input('Ingrese su opcion 1-5: '))

    if opcion == 1:
        clientes = ClienteDAO.seleccionar()
        print(f'***Listado de clientes***')
        for cliente in clientes:
            print(cliente)

    elif opcion == 2:
        print('Ingresa los datos del nuevo cliente')
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        membresia = int(input('Membresia: '))

        cliente =  Cliente(nombre = nombre, apellido= apellido, membresia = membresia)
        clientes_insertados = ClienteDAO.insertar(cliente)
        print(f'Clientes insertados: {clientes_insertados}')

    elif opcion == 3:
        print('Ingresa el id del cliente a modificar ')
        id_cliente = int(input('Id del cliente: '))
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        membresia = input('Membresia: ')

        cliente = Cliente(id = id_cliente,nombre = nombre, apellido = apellido, membresia = membresia)
        cliente_actualizado = ClienteDAO.actualizar(cliente)
        print(f'Clientes actualizados: {cliente_actualizado}')

    elif opcion ==4:
        print('Ingresa el id del cliente a eliminar ')
        id_cliente = int(input('Id del cliente: '))
        cliente = Cliente(id = id_cliente)
        cliente_eliminado = ClienteDAO.eliminar(cliente)
        print(f'Clientes eliminados: {cliente_eliminado}')