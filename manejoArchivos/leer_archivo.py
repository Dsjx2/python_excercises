print('Leer archivo con python\n')

nombre_archivo = 'mi_archivo.txt'

# leer un archivo usando el metodo readlines


for i in range(20):
    with open(nombre_archivo, 'a') as archivo:
        # Anexar informacion al archivo
        archivo.write(f'Anexando informacion... Linea {i} \n ')
        archivo.write('Saliendo de anexar informacion... \n')
    print(f'Se ha anexado infromacion al archivo {nombre_archivo}')



with open(nombre_archivo, 'r') as archivo:
    for i in archivo.readlines():
        print(i.strip())

    # todo = archivo.read()
    # todo = archivo.readlines()

