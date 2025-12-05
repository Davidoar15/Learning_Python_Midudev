# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

sum = 0
count = 1
while count <= 20:
    if count % 2 == 0:
        sum += count
    count += 1

print(sum)
