#Sistema de reserva de hoteles

reserva =  {
"nombre_cliente" : 'Juan Perez',
"dias_estancia" : 3,
"tarifa_diaria" : 23.3,
"tiene_vista_mar" : False,
}

print('Nombre del cliente: ', reserva['nombre_cliente'])
print('Dias de estancia:', reserva['dias_estancia'])
print('Tarifa diaria:', reserva['tarifa_diaria'])
print('Tiene vista al mar:', reserva['tiene_vista_mar'])

for i,val in reserva.items():
    print(type(val))
    print(val)