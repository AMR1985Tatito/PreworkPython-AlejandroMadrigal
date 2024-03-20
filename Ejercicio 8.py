''' 
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.
'''

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Tu Índice de Masa Corporal (IMC) es: {imc:.2f}")