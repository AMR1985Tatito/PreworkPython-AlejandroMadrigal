''' 
Ejercicio 17: Conversor de Millas a Kilómetros
Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros.
'''

def millas_a_kilometros(millas):
    kilometros = millas * 1.60934
    return kilometros

millas = float(input("Ingresa la distancia en millas: "))

kilometros = millas_a_kilometros(millas)

print(f"{millas} millas equivale a {kilometros} kilómetros.")