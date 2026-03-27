#Reemplazar textos en python

mensaje = 'Hola mundo, desde python'

nuevo = mensaje.replace('e','o')

#multiplicacion de cadenas
niveles = int(input())
for i in range(niveles):
    print(" "*(niveles-i),"*"*(2*i-1))