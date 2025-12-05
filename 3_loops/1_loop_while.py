# Simple Condition

# count = 0

# while count <= 5:
#     print(count)
#     count += 1

# # ? break
# # count2 = 0
# # while True:
# #     print(count2)
# #     count2 += 1
# #     if count2 == 6:
# #         break

# # ? continue
# count3 = 0
# while count3 < 10:
#     count3 += 1
#     if count3 % 2 == 0:
#         continue
#     print(count3)

# count4 = 0
# while count4 < 5:
#     print(count4)
#     count4 += 1
#     # break
# else: # condition (count4 < 5) FALSE
#     print("End of WHILE")

# num = -1
# while num < 0:
#     num = int(input("Write a positive number: "))
#     if num < 0:
#         print("Number must be positive. Try again")
# print(f"Number is: {num}")

num = -1
while num < 0:
    try: 
        num = int(input("Write a positive number: "))
        if num < 0:
            print("Number must be positive. Try again")
    except: print("Must be a NUMBER")

print(f"Number is: {num}")