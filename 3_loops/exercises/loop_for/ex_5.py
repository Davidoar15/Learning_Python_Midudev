# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]

letra = input("Por favor, introduzca una letra para buscar: ")
count = 0

for palabra in palabras:
    if letra.lower() == palabra[0].lower(): count += 1
print(f"La cantidad de palabras que empiezan con la letra '{ letra }' es: { count }")
