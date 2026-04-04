nombre_archivo = 'mi_archivo.txt'

try:
    with open(nombre_archivo,'x') as archivo:
        archivo.write('Escritura en modo exclusivo')
        archivo.write('\nEsto es una funcion util')
    print(f'Se ha creado el archivo {nombre_archivo}')
except Exception as e:
    print(f'Error en el archivo {nombre_archivo}')
    print(f'detalle del error {e}')


