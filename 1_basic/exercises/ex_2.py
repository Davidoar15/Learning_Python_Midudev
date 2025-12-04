###
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
vars = [a,b,c,d,e]

for var in vars:
    print(type(var))

# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
