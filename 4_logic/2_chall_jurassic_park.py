"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

def count_total_of_carnivorous_dino_eggs(list_eggs: list[int]):
    total = 0
    for eggs in list_eggs:
        if eggs <= 0: continue
        elif eggs % 2 == 0: total += eggs
    return total

list1 = list(range(11))
list2 = list(range(51))
list3 = list(range(100))

print(count_total_of_carnivorous_dino_eggs(list1))
print(count_total_of_carnivorous_dino_eggs(list2))
print(count_total_of_carnivorous_dino_eggs(list3))
