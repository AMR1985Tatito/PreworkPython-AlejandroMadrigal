''' 
Ejercicio 14: Calculadora de Descuento
Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.
'''

def calcular_precio_final(precio_original, descuento_porcentaje):
    descuento = precio_original * (descuento_porcentaje / 100)
    precio_final = precio_original - descuento
    return precio_final

precio_original = float(input("Ingresa el precio original del artículo: "))

descuento_porcentaje = 20

precio_final = calcular_precio_final(precio_original, descuento_porcentaje)

print(f"El precio final del artículo después de aplicar un descuento del 20% es: {precio_final:.2f} €")