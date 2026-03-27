print("Lista de canciones")

lista_canciones = []

no_songs = int(input('Cuantas canciones desea agregar? '))

for i in range(no_songs):
    cancion = input(f'Ingresa la cancion No. {i+1}: ')
    lista_canciones.append(cancion)

lista_canciones = lista_canciones.sort()

print('Tu lista de canciones es:')
for song in lista_canciones:
    print(song)
