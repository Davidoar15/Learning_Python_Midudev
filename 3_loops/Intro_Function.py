"""
def name_function(param1, param2, ...):
    CODE
    .
    .
    .
    return value (optional)
"""

def say_hi():
    print("HI!")
# say_hi() # HI!

#             param
def say_hi_to(name: str):
    print(f"HI! { name.upper() }")

#         args  
say_hi_to("david")
say_hi_to("mom")

def addition(n1, n2): return n1+n2
print(addition(2, 3)) # 5

# ? docstring (documentation)
def subtract(a, b):
    """Subtracts two numbers and return result"""
    return a - b 

print(subtract.__doc__) # Subtracts two numbers and return result
# help(subtract)

def multiply(c, d=2): return c*d
print(multiply(2)) # 4
print(multiply(2, 3)) # 6

# Args by position
def describe_person(name, age, sex): 
    print(f"I'm { name }, I'm { age } years old and I identify as { sex }")

# positional parameters
describe_person("davidoar", 23, "man") # I'm davidoar, I'm 23 years old and I identify as man
describe_person("man", "davidoar", 1) # I'm man, I'm davidoar years old and I identify as 1

# Args by key 
# Named parameters
describe_person(sex="man", name="davidoar", age=23) # I'm davidoar, I'm 23 years old and I identify as man


# ! Variable length args (*args)
def add_numbers(*args):
    sum = 0
    for num in args: sum += num
    return sum
print(add_numbers(1,2,3,4,5))

# ! Variable key-value args (**kwargs)
# **kwargs: named params but variables
def show_info_of(**kwargs):
    for key, value in kwargs.items():
        print(f"{ key }: { value }")

show_info_of(sex="man", name="davidoar", age=23) # sex: man name: davidoar age: 23
show_info_of(user="david", is_ban=False) # user: david is_ban: False
