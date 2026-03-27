variables = []
variables.append("Curso de Python")
variables.append(23.4)
variables.append(True)
variables.append(False)
variables.append(23)
variables.append((2,3,4,5))
variables.append(['name','age'])
variables.append(({'hola','2',True}))
variables.append(
    {
        'nombre':'Daniel',
        'edad':20,
    }
)



def print_type(var: list):
    for val in var:
        print(type(val))


print_type(variables)
