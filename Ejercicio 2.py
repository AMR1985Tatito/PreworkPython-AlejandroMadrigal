''' 
Ejercicio 2: Calculadora de Propina
Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.
'''

def calcular_total_con_propina(total_cuenta):
    propina = total_cuenta * 0.15
    total_con_propina = total_cuenta + propina
    return total_con_propina

total_cuenta = float(input("Ingresa el total de la cuenta en el restaurante: "))

total_con_propina = calcular_total_con_propina(total_cuenta)

print(f"El total a pagar, incluyendo una propina del 15%, es: {total_con_propina:.2f} €")