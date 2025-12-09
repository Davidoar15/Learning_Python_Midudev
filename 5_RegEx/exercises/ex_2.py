import re
# Validar un correo gmail

email = input("Please, write your gmail: ")
pattern = r"^\w+@gmail.com$"
valid = re.search(pattern, email)
if valid: print("The email is valid!")
else: print("The email is not valid")