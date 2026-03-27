print('Agenda de contactos')


agenda = []

class Persona:
    def __init__(self, nombre,telefono,email,dire):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.dire = dire

agenda_lista = False

while (agenda_lista == False):
    new = int(input('Para ingresar un nuevo registro presiona 1 / cualquier otro para finalizar: '))
    nueva_persona = Persona("","","","")
    if new == 1:
        nueva_persona.nombre = input('Ingrese el nombre del persona: ')
        nueva_persona.telefono = input('Ingrese el telefono del persona: ')
        nueva_persona.email= input('Ingrese el email del persona: ')
        nueva_persona.dire = input('Ingrese el dire del persona: ')

        agenda.append(nueva_persona.__dict__)
    else:
        agenda_lista = True

print('Los contactos de la agenda son: ')
for i,p in enumerate(agenda):
    print(i, f'Nombre:{p['nombre']}, Telefono: {p['telefono']}, Email: {p['email']}, Dire: {p['dire']}')