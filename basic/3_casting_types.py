### Python is strongly typed

print("Type Conversion")

print(type("100"))      # <class 'str'>
print(type(int("100"))) # <class 'int'>

print(type(2 + int("100")), '2 + int("100")', 2 + int("100"), sep=" | ") # <class 'int'> | 2 + int("100") | 102
print(type("100" + str(2)), "'100' + str(2)", "100" + str(2), sep=" | ") # <class 'str'> | '100' + str(2) | 1002

print(type(int(3.14)), "int(3.14)", int(3.14), sep=" | ") # <class 'int'> | int(3.14) | 3

print("bool(3)", bool(3), sep=" | ")   # bool(3) | True
print("bool(0)", bool(0), sep=" | ")   # bool(0) | False
print("bool(-1)", bool(-1), sep=" | ") # bool(-1) | True
#! 0 is the unique number that have falsy value

print('bool("")', bool(""), sep=" | ")           # bool("") | False
print('bool(" ")', bool(" "), sep=" | ")         # bool(" ") | True
print('bool("False")', bool("False"), sep=" | ") # bool("False") | True
#! "" is the unique str that have falsy value

print(type(int(2.5)), "int(2.5)", int(2.5), sep=" | ") # <class 'int'> | int(2.5) | 2
print(round(2.5)) # 2
print(round(3.5)) # 4
print(round(3.6)) # 4
print(round(3.4)) # 3
print(round(2.50000)) # 2
#! 'round()' in case of 'X.5' round to the nearest even number
