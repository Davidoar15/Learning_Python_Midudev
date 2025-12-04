###
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

string = "12345"
string_int = int(string)
string_float = float(string_int)

the_float = 3.99
the_float_to_int = int(the_float)

print(string_int, string_float, the_float_to_int, sep=" | ")
