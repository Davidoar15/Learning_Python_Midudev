###
# int, float, complex
# str
# bool
# NoneType
# list, tuple
# dict
# range
# set ...
###
# (There is no block comment, only "doc string": ''' / """)

print("int:")                                               # int:
print(type(10), 10)                                         # <class 'int'> 10
print(type(-5), -5)                                         # <class 'int'> -5
print(type(9876543345678900987654), 9876543345678900987654) # <class 'int'> 9876543345678900987654

print("float:")         # float:
print(type(3.14), 3.14) # <class 'float'> 3.14
print(type(-1.0), -1.0) # <class 'float'> -1.0
print(type(1e5), 1e5)   # <class 'float'> 100000.0

print("complex:")             # complex:
print(type(1 + 2j), 1 + 2j)   # <class 'complex'> (1+2j)
print(type(1j), 1j)           # <class 'complex'> 1j
print(type(10 + 0j), 10 + 0j) # <class 'complex'> (10+0j)

print("str:")                 # str:
print(type("Hello"), "Hello") # <class 'str'> Hello
print(type(""), "")           # <class 'str'> 
print(type("123"), "123")     # <class 'str'> 123
print(type("""
    Multiline                 
"""))                         # <class 'str'> 

print("bool:")
print(type(True))
print(type(2 == 2), "2 == 2", 2 == 2, sep=" | ")       # <class 'bool'> | 2 == 2 | True
print(type(False))
print(type(1+2 == 2), "1+2 == 2", 1+2 == 2, sep=" | ") # <class 'bool'> | 1+2 == 2 | False

# absence of type
print("NoneType:")        # NoneType:
print(type(None), "None") # <class 'NoneType'> None
