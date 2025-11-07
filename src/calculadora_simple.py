"""
Ejercicio 1: Calculadora Simple
Descripción:
Programa que realiza operaciones básicas entre dos números.
Autor: Sebastian Zapata
Fecha: 2025-11-05
"""

# ============================================
# FUNCIONALIDAD PRINCIPAL
# ============================================

print("=== CALCULADORA SIMPLE ===")

# Intentar capturar entradas válidas
try:
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
except ValueError:
    print("Error: Debes ingresar valores numéricos válidos.")
    exit()  # Finaliza el programa si hay error

# Mostrar menú de operaciones
print("\nOperaciones disponibles:")
print("1. Suma (+)")
print("2. Resta (-)")
print("3. Multiplicación (*)")
print("4. División (/)")
print("5. Salir")

# Pedir operación
operacion = input("\nElige la operación (+, -, *, /): ")

# ============================================
# CONDICIONALES PARA CADA OPERACIÓN
# ============================================

if operacion == "+":
    resultado = numero1 + numero2
    print(f"\nEl resultado de {numero1} + {numero2} es: {resultado}")

elif operacion == "-":
    resultado = numero1 - numero2
    print(f"\nEl resultado de {numero1} - {numero2} es: {resultado}")

elif operacion == "*":
    resultado = numero1 * numero2
    print(f"\nEl resultado de {numero1} × {numero2} es: {resultado}")

elif operacion == "/":
    # Verificar división por cero
    if numero2 == 0:
        print("\nError: No se puede dividir entre cero.")
    else:
        resultado = numero1 / numero2
        print(f"\nEl resultado de {numero1} ÷ {numero2} es: {resultado}")

else:
    print("\nOperación no válida. Debes ingresar +, -, * o /.")

print("\nGracias por usar la calculadora")