# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

age = int(input("How old is the patient? "))

if age >= 65: print("patient: Older adult")
elif age >= 18: print("patient: Adult")
elif age >= 13: print("patient: Teenager")
elif age >= 3: print("patient: Child")
elif age >= 0: print("patient: Baby") 
else: print("ERROR")
