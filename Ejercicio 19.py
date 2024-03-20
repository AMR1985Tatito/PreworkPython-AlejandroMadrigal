''' 
Ejercicio 19: Verificación de Año Bisiesto
Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.
'''

def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

anio = int(input("Ingresa un Año para verificar si es Bisiesto: "))

if es_bisiesto(anio):
    print(f"{anio} es un Año Bisiesto.")
else:
    print(f"{anio} no es un Año Bisiesto.")