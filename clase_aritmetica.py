print('***Clases***')


class Aritmetica():
    def __init__(self,a:int,b:int):
        self.a = a
        self.b = b

    def sumar(self):
        result = self.a + self.b
        print(f'Resultado {result}')

    def restar(self):
        result = self.a - self.b
        print(f'Resultado {result}')
    def multiplicar(self):
        result = self.a * self.b
        print(f'Resultado {result}')
    def dividir(self):
        result = self.a / self.b
        print(f'Resultado {result}')

# Instancia objeto 1

ari1 = Aritmetica(3,4)
ari1.sumar()
ari1.restar()
ari1.multiplicar()
# Otro objeto instanciado
ari2 = Aritmetica(3,5)
ari2.sumar()
ari2.restar()
ari2.multiplicar()