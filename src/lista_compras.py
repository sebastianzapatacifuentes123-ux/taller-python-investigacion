"""
Ejercicio 3: Lista de Compras
Descripción:
El programa pide al usuario cuántos productos va a comprar,
solicita nombre y precio de cada uno, calcula el total a pagar
y aplica un 10% de descuento si el total supera $100.
Autor: Sebastian Zapata
Fecha: 2025-11-05
"""

print("=== LISTA DE COMPRAS ===\n")

# Pedir la cantidad de productos
try:
    cantidad = int(input("¿Cuántos productos vas a comprar? "))
except ValueError:
    print("Debes ingresar un número válido.")
    exit()

# Lista para guardar los productos
productos = []
total = 0

# Ciclo para pedir nombre y precio de cada producto
for i in range(cantidad):
    print(f"\nProducto #{i + 1}")

    nombre = input("Nombre del producto: ")

    try:
        precio = float(input("Precio del producto ($): "))
        if precio < 0:
            print("El precio no puede ser negativo. Se omitirá este producto.")
            continue
    except ValueError:
        print("Precio inválido. Se omitirá este producto.")
        continue

    productos.append((nombre, precio))
    total += precio

# Mostrar resumen de compra
print("\n=== RESUMEN DE COMPRA ===")

if not productos:
    print("No se ingresaron productos válidos.")
    exit()

for nombre, precio in productos:
    print(f"- {nombre}: ${precio:.2f}")

print(f"\nSubtotal: ${total:.2f}")

# Aplicar descuento si el total supera $100
if total > 100:
    descuento = total * 0.10
    total_con_descuento = total - descuento
    print(f"Descuento aplicado (10%): -${descuento:.2f}")
    print(f"✅ Total a pagar con descuento: ${total_con_descuento:.2f}")
else:
    print("No aplica descuento.")
    print(f"Total a pagar: ${total:.2f}")

print("\nGracias por tu compra")