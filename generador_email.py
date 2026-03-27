#Generador de emails

nombre = input("Escribe tu nombre: ")
empresa = input("Escribe la empresa: ")

def generar_email(nombre:str, empresa:str):
    nombre = nombre.replace(" ",".").lower()
    empresa = empresa.replace(" ","").lower()
    return f'{nombre}@{empresa}.com.gt'

print(generar_email(nombre, empresa))