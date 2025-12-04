#print("Hi, what is your name?")

# ! Get user data from stdin / standard input
#name = input() -> ALWAYS STR

name = input("Hi, what is your name? \t")

#print("\nHello "+name+"!")
print(f"Hello {name}!\n")

age = input("How old are you?\t")
print(f"In twenty years you will have { int(age) + 20 }\n")

# Get multiple values
country, city = input("What country and city do you live?\t").split()
print(f"So, you live in { city }, { country }")