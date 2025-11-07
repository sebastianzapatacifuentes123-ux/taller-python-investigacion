"""
Ejercicio 2: Adivina el número
Descripción:
El usuario debe adivinar un número secreto aleatorio entre 1 y 50.
Tiene un máximo de 5 intentos.
Autor: Sebastian Zapata
Fecha: 2025-11-06
"""

# ============================================
# IMPORTAR MÓDULOS
# ============================================
import random

# ============================================
# CONSTANTES
# ============================================
MAX_INTENTOS = 5
NUMERO_SECRETO = random.randint(1, 50)  # Número aleatorio entre 1 y 50

# ============================================
# VARIABLES INICIALES
# ============================================
intento = 0
adivinado = False

print("===  ¡ADIVINA EL NÚMERO! ===")
print("Estoy pensando en un número entre 1 y 50 ")

# ============================================
# CICLO PRINCIPAL
# ============================================
while intento < MAX_INTENTOS and not adivinado:
    try:
        numero = int(input(f"\nIntento {intento + 1} de {MAX_INTENTOS}: Ingresa tu número: "))
    except ValueError:
        print("Por favor, ingresa solo números enteros.")
        continue  # No cuenta como intento fallido

    intento += 1

    if numero == NUMERO_SECRETO:
        print(f" ¡Felicitaciones! Adivinaste el número secreto ({NUMERO_SECRETO}) en {intento} intento(s).")
        adivinado = True
    elif numero < NUMERO_SECRETO:
        print("El número secreto es mayor.")
    else:
        print("El número secreto es menor.")

# ============================================
# MENSAJE FINAL
# ============================================
if not adivinado:
    print("\nLo siento, has agotado tus intentos.")
    print(f"El número secreto era: {NUMERO_SECRETO}")

print("\nGracias por jugar ")