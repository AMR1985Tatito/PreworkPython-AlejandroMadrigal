''' 
Ejercicio 9: Conversor de Divisas
Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.
'''

def dolares_a_euros(dolares):
    euros = dolares * 0.85
    return euros

dolares = float(input("Ingresa la cantidad de dólares a convertir a euros: "))

euros = dolares_a_euros(dolares)

print(f"{dolares} dólares equivalen a {euros} euros.")