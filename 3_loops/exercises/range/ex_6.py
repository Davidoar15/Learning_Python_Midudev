# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")

num = int(input("Please, write a number: "))

for n in range(1, 11):
    print(f"{ num } x { n } = { num*n }")
