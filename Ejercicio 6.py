''' 
Ejercicio 6: Verificación de Palíndromo
Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
'''

def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    if palabra == palabra[::-1]:
        return True
    else:
        return False

palabra = input("Ingresa una palabra para verificar si es un palíndromo: ")

if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo.")
else:
    print(f"'{palabra}' no es un palíndromo.")