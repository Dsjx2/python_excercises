class Persona:
    #Atributos de la clase
    contador_personas = 0

    def __init__(self, name, lastname):
        #Incrementamos el valor del atributo de la clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.name = name
        self.lastname = lastname

    def mostrar_persona(self):
        print(f'Persona: {self.id}, Name: {self.name}, Lastname: {self.lastname}')


if __name__ == '__main__':
    print(f'Ejemplo de contador  de objetos de tipo persona')
    persona1 = Persona('Daniel', 'Subu')
    persona1.mostrar_persona()

    print(f'Ejemplo de contador  de objetos de tipo persona')
    persona2 = Persona('Daniel', 'Subu')
    persona2.mostrar_persona()

    print(f'Contador de personas {Persona.contador_personas}')