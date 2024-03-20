''' 
Ejercicio 4: Contador de Vocales
Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario
'''

def contar_vocales(palabra):
    palabra = palabra.lower()
    vocales = ['a', 'e', 'i', 'o', 'u']
    contador_vocales = 0
    for letra in palabra:
        if letra in vocales:
            contador_vocales += 1
    return contador_vocales

palabra = input("Ingresa una palabra: ")

numero_vocales = contar_vocales(palabra)

print(f"'{palabra}' tiene {numero_vocales} vocales")