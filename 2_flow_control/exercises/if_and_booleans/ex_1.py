# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

num1, num2 = input("Please two numbers:\t").split()

if num1 > num2:
    print(f"{ num1 } es mayor que { num2 }")
elif num1 < num2:
    print(f"{ num2 } es mayor que { num1 }")
else: 
    print("Both numbers are equal")