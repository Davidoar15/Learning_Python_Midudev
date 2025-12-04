list1 = [1,2,3,4,5]
list_chars = ["apple", "banana", "peach"]
list_multp: list[int | str | float | bool] = [1, "hi", 3.14, True]

empty_list = []

list_of_lists = [[1, 2], [3, 4]]

matrix = [[1, 2], [3, 4], [5, 6]]

print(list1)
print(list_chars)
print(list_multp)
print(empty_list)
print(list_of_lists)
print(matrix)

print(list_chars[1]) # banana
print(list_chars[-1]) # peach
print(list_chars[-3]) # apple

print(list_of_lists[1][0]) # 3

# ? Slicing
print(list1[1:4]) # [2,3,4]
print(list1[:3]) # [1,2,3]
print(list1[2:]) # [3,4,5]
print(list1[:]) # [1,2,3,4,5] COPY OF LIST1

superlist = [1,2,3,4,5,6,7,8]

print(superlist[::2]) # [1, 3, 5, 7] | superlist(from:to:STEP)
print(superlist[::-1]) # [8, 7, 6, 5, 4, 3, 2, 1]

# ! Modify list
list1[1] = 20
print(list1) # [1, 20, 3, 4, 5]

# ! Add elem
list2 = [-2, -1, 0]
# list2 = list2 + list1 . BETTER:
list2 += list1
print(list2) # [-2, -1, 0, 1, 20, 3, 4, 5]