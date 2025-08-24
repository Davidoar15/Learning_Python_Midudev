### Python is a dynamically typed language

my_nickname = "davidoar15"

print(my_nickname) # davidoar15

age = 22
print(age) # 22
age = 23
print(age) # 23

nickname = "davidoar15"
print(type(nickname), nickname) # <class 'str'> davidoar15
nickname = 15
print(type(nickname), nickname) # <class 'int'> 15

#! f-string
print(f"Hello, I'm {my_nickname}, I am {age} years old") # Hello, I'm davidoar15, I am 23 years old

#? Other way of asignation (not recomended)
nombre, edad, ciudad = "david", 23, "Maracay"
print(nombre, edad, ciudad, sep=" - ") # david - 23 - Maracay

#? Variable naming conventions
# snake_case !!!
my_variable_name = "ok"

# PascalCase
MyVariableName = "ok2"
# flatcase
myvariablename = "ok3"

### Python not have CONST
#! UPPER_CASE
MY_CONST_PI = 3.14
print(MY_CONST_PI)

### All Keywords of Python
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 
# 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 
# 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 
# 'raise', 'return', 'try', 'while', 'with', 'yield']
