fruits = ["apple", "pear", "banana"]
for fruit in fruits:
    print(fruit)

string = 'string'
for char in string:
    print(char)


# ? enumerate()
for index, fruit in enumerate(fruits):
    print(f"Index: { index } and Fruit: { fruit }")


letters = ['a', 'b', 'c']
numbers = [1,2,3]

for letter in letters:
    for number in numbers:
        print(f"{ letter } x { number }")

animals = ["dog", "cat", "bird", "spider", "bug"]
for i, animal in enumerate(animals): 
    print(animal)
    if animal == "bird":
        print(f"A bird found in index: { i }")
        break

for i, animal in enumerate(animals): 
    if animal == "bird": continue

    print(i, animal)


# List Comprehension       animal      =      animal
animals_capital_letters = [animal.upper() for animal in animals]
print(animals_capital_letters)


# Show even numbers (List Comprehension + Conditional)
even = [num for num in [1,2,3,4,5,6,7,8,9] if num % 2 == 0]
print(even)