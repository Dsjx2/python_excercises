# Manejo de archivos

nombre_archivo = 'mi_archivo.txt'
# Abrir archivo en modo escritura "w"

# uso de with con open
with open(nombre_archivo,'w') as archivo:
    archivo.write('Hola como estas')
    archivo.write('\nEstoy agregando informacion al archivo')


#Abrir un archivo en modo exclusivo




# archivo = open(nombre_archivo,'w')
# archivo.write('Hola como estas\n')
# archivo.write('Estoy agregando informacion al archivo')
# archivo.close()

print(f'Se creo el archivo: {nombre_archivo}')
