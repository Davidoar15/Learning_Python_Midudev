# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

year = input("Please, write a year: ")
actual_year = int(year)

year_divisible_4 = actual_year % 4 == 0
year_divisible_100 = actual_year % 100 == 0
year_divisible_400 = actual_year % 400 == 0

if year_divisible_4:
    if year_divisible_100 and not year_divisible_400: print(f"{ year } is not leap")
    else: print(f"{ year } is leap!")
else: print(f"{ year } is not leap")
