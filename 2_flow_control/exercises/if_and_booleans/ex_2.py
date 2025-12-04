# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

SUMA = '+'
RESTA = '-'
MULTIPLICACION = '*'
DIVISION = '/'

num1, num2, op = input("Por favor 2 numeros y por ultimo alguna operacion (+, -, *, /): ").split()

n1 = int(num1)
n2 = int(num2)

if op == SUMA:
    print(f"Resultado: { n1 + n2 }")
elif op == RESTA:
    print(f"Resultado: { n1 - n2 }")
elif op == MULTIPLICACION:
    print(f"Result: { n1 * n2 }")
elif op == DIVISION:
    if n2 == 0: print("ERROR FATAL. NO ES POSIBLE LA DIVISION POR 0")
    else: print(f"Result: { n1/n2 }")
else: 
    print(f"ERROR FATAL. '{ op }' NO ES UNA OPERACION PERMITIDA")

