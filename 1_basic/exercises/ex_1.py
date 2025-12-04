###
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

name: str = input("Hi, what is your name?\t")
city: str = input("and, where do you live?\t")

print(f"So, you are { name } and live in { city }")
