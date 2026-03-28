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

    @staticmethod
    def get_contador_personas_estatico():
        print(f'Metodo estatico')
        return Persona.contador_personas

    @classmethod
    def get_contador_personas_clase(cls):
        print(f'Metodo de clase')
        return cls.contador_personas



if __name__ == '__main__':
    print(f'Ejemplo de contador  de objetos de tipo persona')
    persona1 = Persona('Daniel', 'Subu')
    persona1.mostrar_persona()

    print(f'Ejemplo de contador  de objetos de tipo persona')
    persona2 = Persona('Daniel', 'Subu')
    persona2.mostrar_persona()

    print(f'Contador de objetos persona {Persona.contador_personas}')
    print(f'Contador de objetos Persona (static) {Persona.get_contador_personas_estatico()}')
    print(f'Contador de objetos Persona (clase) {Persona.get_contador_personas_clase()}')