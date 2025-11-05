"""
Ejercicio Básico: Calculadora de Edad
Practica con variables, input, y operaciones básicas
"""
# CONSTANTES
ANIO_ACTUAL = 2025
# Solicitar datos al usuario
print("=== CALCULADORA DE EDAD ===")
nombre = input("Tu nombre: ")
anio_nacimiento = input("¿En qué año naciste? ")
# Convertir texto a número
anio_nacimiento = int(anio_nacimiento)
# Calcular la edad
edad = ANIO_ACTUAL - anio_nacimiento
# Mostrar resultado
print(f"\nHola {nombre}, tienes {edad} años")
# Usar condicional
if edad >= 18:
 print("Eres mayor de edad")
else:
 print("Eres menor de edad")
 anos_faltantes = 18 - edad
 print(f"Te faltan {anos_faltantes} años para ser mayor de edad")