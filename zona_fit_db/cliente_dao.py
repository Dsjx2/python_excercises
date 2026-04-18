from zona_fit_db.conexion import Conexion
from cliente import Cliente


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES (%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre = %s, apellido = %s, membresia = %s WHERE id = %s'
    DELETE = 'DELETE FROM cliente WHERE id = %s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase - tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes
        except Exception as e:
            print(f'Ocurió un error al seleccionar clientes {e}')
            return None
        finally:
            if cursor is not None:
                cursor.close()
                if conexion is not None:
                    Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        cursor = None

        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre,cliente.apellido,cliente.membresia)
            cursor.execute(cls.INSERTAR,valores)
            conexion.commit()
            return cursor.rowcount
            # conexion.row
            # print(f'Se ha agregado un nuevo registro {cliente}')
        except Exception as e:
            print(f'Ha ocurrido un error al insertar cliente {e}')
        finally:
            if cursor is not None:
                cursor.close()
                if conexion is not None:
                    Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f'Ha ocurrido un error al actualizar cliente {e}')
        finally:
            if cursor is not None:
                cursor.close()
                if conexion is not None:
                    Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.id,)
            cursor.execute(cls.DELETE, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f'Ha ocurrido un error al eliminar cliente {e}')
        finally:
            if cursor is not None:
                cursor.close()
                if conexion is not None:
                    Conexion.liberar_conexion(conexion)


# if __name__ == '__main__':
#
#     # #Insertar Nuevo
#     # nombre = input('Ingrese el nombre a ingresar: ')
#     # apellido = input('Ingrese su apellido: ')
#     # membresia = input('Monto de la membresia: ')
#     #
#     # nuevo_cliente = Cliente(nombre =nombre, apellido=apellido,membresia=membresia)
#     # clientes_insertados = ClienteDAO.insertar(nuevo_cliente)
#     # print(f'Clientes insertados: {clientes_insertados}')
#
#     # #Actualizar Cliente
#     # actualizar_cliente = Cliente(1, 'Alexandre', 'Vinicius', 300)
#     # clientes_actualizados = ClienteDAO.actualizar(actualizar_cliente)
#     # print(f'Clientes actualizados: {clientes_actualizados}')
#
#     #Eliminar Cliente
#
#     eliminar_cliente = Cliente(id = 1)
#     cliente_eliminado = ClienteDAO.eliminar(eliminar_cliente)
#     print(f'Cliente eliminado {cliente_eliminado}')
#
#     #Seleccionar todo
#     clientes = ClienteDAO.seleccionar()
#     for cliente in clientes:
#         print(cliente)
