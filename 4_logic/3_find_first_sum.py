"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

def find_first_sum(nums, goal) -> list[int] | None: 
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == goal: return [i, j]
    return None

# def meet_condition(num1: int, num2: int, goal: int) -> bool: 
#     """
#     Verifies that both numbers are distinct and their sum is equal goal
#     """
#     return num1 != num2 and num1 + num2 == goal

print(find_first_sum([4, 5, 6, 2], 8))
print(find_first_sum([4, 6, 6, 2], 11))
