''' 
Ejercicio 1: Conversor de Temperatura
Escribe un programa que convierta una temperatura de grados Celsius a grados
Fahrenheit. 
'''

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius = float(input("Ingresa la temperatura en Grados Celsius: "))

fahrenheit = celsius_a_fahrenheit(celsius)

print(f"{celsius} Grados Celsius equivalen a {fahrenheit} Grados Fahrenheit.")