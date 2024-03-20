''' 
Ejercicio 12: Calculadora de Área de un Rectángulo
Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo.
'''

def calcular_area_rectangulo(longitud, ancho):
    area = longitud * ancho
    return area

longitud = float(input("Ingresa la longitud del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))

area_rectangulo = calcular_area_rectangulo(longitud, ancho)

print(f"El área del rectángulo es: {area_rectangulo}")