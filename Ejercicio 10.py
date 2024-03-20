''' 
Ejercicio 10: Determinar el Día de la Semana
Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).
'''

def determinar_dia_semana(numero):
    if numero == 1:
        return "Lunes"
    elif numero == 2:
        return "Martes"
    elif numero == 3:
        return "Miércoles"
    elif numero == 4:
        return "Jueves"
    elif numero == 5:
        return "Viernes"
    elif numero == 6:
        return "Sábado"
    elif numero == 7:
        return "Domingo"
    else:
        return "Número inválido. Debe ser un número entre 1 y 7."

numero = int(input("Ingresa un número del 1 al 7 para determinar el día de la semana: "))

dia_semana = determinar_dia_semana(numero)

print(f"El número {numero} corresponde a {dia_semana}.")