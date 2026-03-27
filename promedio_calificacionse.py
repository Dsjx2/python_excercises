print('Sistema de calculo de promedio')

no_cursos = int(input("Ingresa la cantidad de cursos"))

cursos = []

for curso in range(no_cursos):
    nota_curso = float(input("Ingrese su nombre_curso"))
    cursos.append(nota_curso)

print('calculo del promedio: ')

promedio = (sum(cursos)/len(cursos))
print(f'El promedio de los cursos es: {promedio:.2f}')