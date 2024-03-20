''' 
Ejercicio 20: Suma de Números en una Lista
Crea un programa que sume todos los números en una lista ingresada por el
usuario.
'''

def sumar_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

entrada = input("Ingresa los números de la lista separados por comas: ")

lista_numeros = [float(x) for x in entrada.split(',')]

suma_total = sumar_lista(lista_numeros)

print(f"La suma de todos los números en la lista es: {suma_total}")