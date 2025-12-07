nums = range(5) # ! "range" DOES NOT CREATE A LIST
print(type(nums), nums, sep=" | ") # <class 'range'> | range(0, 5)
# print(type([])) # <class 'list'>

#            (0, 10, 1)
nums2 = range(10) # ! GENERATES A NUMBER SEQUENCE FROM 0 TO 9
for num in nums2: # ? or for num in range(10):
    print(num)

for n in range(5, 10):
    print(n)

#             (start, end, STEP) 
for n in range(    0,  10,    2):
    print(n)

for n in range(-5, 0): print(n)
for n in range(10, 0, -1): print(n)

ns = range(10)
list_of_ns = list(ns)
print(type(list_of_ns), list_of_ns, sep=" | ") # <class 'list'> | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# count = 0
# while count < 5:
#     print("something")
#     count += 1

# BETTER with "range"
for _ in range(5): print("something")
