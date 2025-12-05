lista = ['a', 'b', 'c', 'd']

lista.append('e') # add elem at final
lista.insert(1, '@') # add elem at first arg (index)
print(lista) # ['a', '@', 'b', 'c', 'd', 'e']

lista.extend(['f', 'g']) # add elems at final
print(lista) # ['a', '@', 'b', 'c', 'd', 'e', 'f', 'g']


lista.remove('@') # delete FIRST '@' that appears
print(lista) # ['a', 'b', 'c', 'd', 'e', 'f', 'g']

last = lista.pop() # delete and return elem of list. Default: delete last elem
print(lista) # ['a', 'b', 'c', 'd', 'e', 'f']
print(last) # g

lista.pop(-2)
print(lista) # ['a', 'b', 'c', 'd', 'f']

lista.clear() # delete ALL elems of list
print(lista) # []

animals = ['dog', 'cat', 'horse', 'fish', 'spider']
del animals[3:]
print(animals) # ['dog', 'cat', 'horse']


numbers = [2, 10, 17, 9, 99, 201]
# numbers.sort() # DOES MODIFY Original List
# print(numbers) # [2, 9, 10, 17, 99, 201]

# ? Copy of list modified
sorted_numbers = sorted(numbers) # DOES NOT Modify numbers
print(sorted_numbers)

fruit = ['apple', 'peach', "pear", "banana", "zapote"]
sorted_fruit = sorted(fruit)
print(sorted_fruit) # ['apple', 'banana', 'peach', 'pear', 'zapote']

fruit[4] = "Zapote"
sorted_fruit2 = sorted(fruit)
print(sorted_fruit2) # ['Zapote', 'apple', 'banana', 'peach', 'pear'] !!

fruit.sort(key=str.lower)
print(fruit) # ['apple', 'banana', 'peach', 'pear', 'Zapote']


animals2 = ['dog', 'cat', 'fish', 'dog']
print(animals2.count('dog')) # 2
print('fish' in animals2) # True
