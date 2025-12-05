# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas

frutas = ["Manzana", "pera", "BANANA", "naranja"]

frutas.sort(key=str.lower)
print(frutas)
