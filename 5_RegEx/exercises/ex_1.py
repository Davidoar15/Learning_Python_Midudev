import re
# Detectar si hay un numero de Argentina en el texto gracias al prefijo +54

text = input("My number phone is: ")
found = re.search(r"\+54 \d{10}", text)
if found: print("Number phone detected: { found.group() }")
else: print("No Argentine phone number was detected")
