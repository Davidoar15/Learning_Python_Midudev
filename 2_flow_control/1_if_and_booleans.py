# from os import system
# if system("clear") != 0: system("cls")

# if, else, elif (else if)

age = 18

# if age >= 18: print("You are of legal age.")
if age >= 18: 
    print("You are of legal age.")
    print("Congrats")

other_age = 16

if other_age >= 18:
    print("You are of legal age.")
else:
    print("You are underage")

grade = 7
if grade >= 8:
    print("Outstanding!")
elif grade >= 6:
    print("Approved!")
else:
    print("Failed")

actual_age = 23
have_DNI = True

if actual_age >= 18 and have_DNI:
    print("You can drive!")
else:
    print("You can't drive")
# && = and
# || = or
#/ ! = not

#! lexicographical comparison
print("manzana < pera:", "manzana" < "pera") # True
print("zapote < pera:", "zapote" < "pera") # False
print("a < c:", ord("a") < ord("c")) # True

# ? Ternary
# {CODE IF CONDITION == TRUE} if {CONDITION} else {CODE IF CONDITION == FALSE} 

brother_age = 17
msj = "You are of legal age." if brother_age >= 18 else "You are underage."
print(msj)