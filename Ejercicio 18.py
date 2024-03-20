''' 
Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.
'''

def contar_palabras(oracion):
    palabras = oracion.split()
    cantidad_palabras = len(palabras)
    return cantidad_palabras

oracion = input("Ingresa una oración para contar la cantidad de palabras que tiene: ")

cantidad_palabras = contar_palabras(oracion)

print(f"La cantidad de palabras que tiene la oración es: {cantidad_palabras}")