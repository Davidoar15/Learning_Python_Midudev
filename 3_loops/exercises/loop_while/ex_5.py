# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

num = int(input("Write a number to print its multiplication table: "))
count = 1

while count <= 10:
    print(f"{ count } * { num } = { num*count }")
    count += 1
