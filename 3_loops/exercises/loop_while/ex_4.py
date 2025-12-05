# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

while True:
    password = input("Please, write a password (8 chars min.): ")
    if len(password) >= 8:
        print("Valid Password!")
        break
    else: print("Few chars, try again")
