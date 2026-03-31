class Persona:
    def __init__(self,nombre , apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'''Persona:
        nombre = {self.nombre}
        apellido = {self.apellido}
        Dir. mem. {super.__str__(self)}
        '''

persona1 = Persona("Daniel","Subuyuj")
print(persona1)
