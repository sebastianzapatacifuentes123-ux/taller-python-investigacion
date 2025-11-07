"""
Ejercicio: Practicando Ciclos
Diferentes ejemplos de for y while
"""
print("=== EJERCICIO 1: CONTAR NÚMEROS ===")
# Ciclo for simple
for i in range(1, 6):
 print(f"Contando: {i}")
print("\n=== EJERCICIO 2: SUMA ACUMULATIVA ===")
# Usar una variable acumuladora
suma = 0
for numero in range(1, 11):
 suma = suma + numero
 print(f"Suma hasta {numero}: {suma}")
print(f"\nTotal final: {suma}")
print("\n=== EJERCICIO 3: PEDIR NÚMEROS ===")
# Ciclo while con condición
contador = 0
while contador < 5:
 numero = input(f"Dame el número {contador + 1}: ")
 print(f"Guardaste: {numero}")
 contador = contador + 1
print("\n=== EJERCICIO 4: NÚMEROS PARES ===")
# Mostrar solo números pares
print("Números pares del 1 al 20:")
for num in range(1, 21):
 if num % 2 == 0: # % es el operador módulo (residuo)
    print(num, end=" ")
print() # Salto de línea al final