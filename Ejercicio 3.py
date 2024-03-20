''' 
Ejercicio 3: Verificación de Edad
Escribe un programa que solicite la edad de un usuario y determine si es mayor de
edad (mayor o igual a 18 años) o no.
'''

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

edad = int(input("Ingresa tu Edad: "))

if es_mayor_de_edad(edad):
    print("Eres mayor de edad")
else:
    print("Eres menor de edad.")