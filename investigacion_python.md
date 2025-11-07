INVESTIGACIÓN OBLIGATORIA SOBRE PYTHON

1. ¿Qué es una variable en Python?
   DESARROLLO
   una variable es un espacio en memoria donde se almacena un valor que puede cambiar durante la ejecución del programa.
   Se crea al asignar un valor con el operador =.
   -Tipos de datos que puede almacenar:
   int: números enteros (10, -3)
   float: números decimales (3.14, -2.5)
   str: cadenas de texto ("Hola", 'Python')
   bool: valores lógicos (True, False)
   -Ejemplos:
   Nombres válidos:
   nombre = "Sebastian"
   edad_2025 = 20
   es_estudiante = True
   Nombres inválidos:
   2nombre = "Error" # no puede empezar con número
   mi-variable = 10 # el guion no está permitido
   print = "texto" # sobrescribe una función reservada

2. ¿Qué diferencia hay entre = y == en Python?
   DESARROLLO
   = (asignación): se usa para guardar un valor en una variable.
   == (comparación): se usa para verificar si dos valores son iguales.
   Ejemplo:
   x = 5 # Asigna el valor 5 a x
   y = 5
   print(x == y) # Devuelve True porque ambos son iguales

3. ¿Qué es la indentación en Python y por qué es importante?
   DESARROLLO
   La indentación es el espacio que se deja al inicio de las líneas dentro de estructuras como if, for, while, def, etc.
   Python usa la indentación para definir bloques de código, no llaves {} como otros lenguajes.
   Ejemplo correcto:
   if edad >= 18:
   print("Eres mayor de edad")
   Ejemplo incorrecto (sin indentación):
   if edad >= 18:
   print("Eres mayor de edad")
   Esto generará un error IndentationError.

4. Diferencia entre ciclo for y ciclo while
   DESARROLLO
   -ciclo for: se usa cuando se conoce el número exacto de repeticiones. Usa una secuencia (lista, rango, etc). Por ejemplo, si queremos mostrar los números del 1 al 5, usando un rango con for:
   for numero in range(1, 6):
   print(numero)
   -ciclo while: se usa cuando se repite algo hasta que un condición deje de cumplirse. Se detiene solo cuando la condición es falsa. Por ejemplo, si queremos contar hasta 5 usando una variable que va aumentando:
   contador = 1
   while contador <= 5:
   print(contador)
   contador += 1

5. ¿Qué hace la función range() en Python?
   DESARROLLO
   La función range() genera una secuencia de números enteros consecutivos, que se usa normalmente con el ciclo for.
   Ejemplos:
   range(5) # genera 0, 1, 2, 3, 4. Por defecto empieza en 0 y llega hasta 4, porque el numero final no se incluye.
   range(1, 10) # genera 1, 2, 3, ..., 9
   range(0, 10, 2) # genera 0, 2, 4, 6, 8 (de 2 en 2) el tercer valor indica de cuanto en cuanto se contará.
