class Persona:
    atributo_clase = 0


    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia


if __name__ == '__main__':
    print('Atributos de clase')
    print(f'Atributo de clase :  {Persona.atributo_clase}')

    #Modificamos el atributo de clase
    Persona.atributo_clase = 30
    print(f'Atributo de clase actual :  {Persona.atributo_clase}')

    #Creamos un objeto p1
    p1 = Persona(123)
    print(f'Atributo de clase desde p1 :  {p1.atributo_clase}')
    print(f'Atributo de instancia desde p1: {p1.atributo_instancia}')


    #creacion de p2
    p2 = Persona(32)
    print(f'Atributo de clase desde p2 :  {p2.atributo_clase}')
    print(f'Atributo de instancia desde p2: {p2.atributo_instancia}')