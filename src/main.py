"""
Programa: Hola Mundo Interactivo
Descripción: Programa que saluda al usuario, pregunta su edad
y muestra un menú con opciones usando condicionales y ciclos.
Autor: [Tu Nombre]
Fecha: 2025-11-03
"""

# ==========================================
# CONSTANTES DEL PROGRAMA
# ==========================================
NOMBRE_PROGRAMA = "Hola Mundo Interactivo"
VERSION = "1.0"
MAX_INTENTOS = 3
ANIO_ACTUAL = 2025

# ==========================================
# SALUDO INICIAL
# ==========================================
print("=" * 50)
print(f"    {NOMBRE_PROGRAMA} v{VERSION}")
print("=" * 50)
print()

# Pedir el nombre del usuario
nombre_usuario = input("¿Cuál es tu nombre? ")

# Validar si el usuario ingresó algo
if nombre_usuario.strip() == "":
    print("No ingresaste un nombre,Te llamaré 'Usuario'.")
    nombre_usuario = "Usuario"
else:
    print(f"¡Hola, {nombre_usuario}! Bienvenido/a al programa.")

print()

# ==========================================
# PREGUNTAR LA EDAD
# ==========================================
edad_texto = input("¿Cuántos años tienes? ")
edad = int(edad_texto)

# Clasificar al usuario
if edad < 18:
    categoria = "joven"
    print(f"Eres menor de edad, {nombre_usuario}.")
elif edad < 60:
    categoria = "adulto"
    print(f"Eres adulto, {nombre_usuario}.")
else:
    categoria = "adulto mayor"
    print(f"Eres adulto mayor, {nombre_usuario}.")

# Calcular año de nacimiento
anio_nacimiento = ANIO_ACTUAL - edad
print(f"Naciste aproximadamente en el año {anio_nacimiento}.")
print()

# ==========================================
# MENÚ DE OPCIONES
# ==========================================
print("=" * 50)
print("MENÚ DE OPCIONES")
print("=" * 50)
print("1. Ver tu información")
print("2. Contar del 1 al 10")
print("3. Tabla de multiplicar")
print("4. Salir")
print("=" * 50)

continuar = True
intentos_fallidos = 0

# ==========================================
# CICLO PRINCIPAL DEL MENÚ
# ==========================================
while continuar:
    opcion = input("\nElige una opción (1-4): ")

    # OPCIÓN 1: Mostrar información del usuario
    if opcion == "1":
        print("\n--- TU INFORMACIÓN ---")
        print(f"Nombre: {nombre_usuario}")
        print(f"Edad: {edad} años")
        print(f"Categoría: {categoria}")
        print(f"Año de nacimiento: {anio_nacimiento}")
        intentos_fallidos = 0

    # OPCIÓN 2: Contar del 1 al 10
    elif opcion == "2":
        print("\n--- CONTANDO DEL 1 AL 10 ---")
        for numero in range(1, 11):
            print(f"Número: {numero}")
        intentos_fallidos = 0

    # OPCIÓN 3: Tabla de multiplicar
    elif opcion == "3":
        numero_tabla = input("\n¿De qué número quieres la tabla? ")
        numero_tabla = int(numero_tabla)
        print(f"\n--- TABLA DEL {numero_tabla} ---")
        for i in range(1, 11):
            resultado = numero_tabla * i
            print(f"{numero_tabla} x {i} = {resultado}")
        intentos_fallidos = 0

    # OPCIÓN 4: Salir del programa
    elif opcion == "4":
        print(f"\n¡Hasta luego, {nombre_usuario}!")
        print("Gracias por usar el programa.")
        continuar = False

    # OPCIÓN INVÁLIDA
    else:
        intentos_fallidos += 1
        print(f"\nOpción inválida. Intento {intentos_fallidos} de {MAX_INTENTOS}")
        if intentos_fallidos >= MAX_INTENTOS:
            print("Demasiados intentos fallidos. Cerrando programa...")
            continuar = False

# ==========================================
# MENSAJE FINAL
# ==========================================
print("\n" + "=" * 50)
print("PROGRAMA FINALIZADO")
print("=" * 50)