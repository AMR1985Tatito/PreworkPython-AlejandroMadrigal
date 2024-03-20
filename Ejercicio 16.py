''' 
Ejercicio 16: Contador de Números Pares e Impares
Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.
'''

def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

entrada = input("Ingresa los números de la lista separados por comas: ")

lista_numeros = [int(x) for x in entrada.split(',')]

cantidad_pares, cantidad_impares = contar_pares_impares(lista_numeros)

print(f"En la lista ingresada hay {cantidad_pares} números pares y {cantidad_impares} números impares.")