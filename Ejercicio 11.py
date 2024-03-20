''' 
Ejercicio 11: Calculadora de Edad
Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.
'''

from datetime import datetime

def calcular_edad(fecha_nacimiento):
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad

anio_nacimiento = int(input("Ingresa tu año de nacimiento (AAAA): "))

fecha_nacimiento = datetime(anio_nacimiento, 1, 1)

edad_actual = calcular_edad(fecha_nacimiento)

print(f"Tienes {edad_actual} años de edad.")