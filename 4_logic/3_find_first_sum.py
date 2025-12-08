"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

def find_first_sum(nums, goal) -> list[int] | None: 
    for i, n1 in enumerate(nums):
        for j, n2 in enumerate(nums):
            if meet_condition(n1, n2, goal): return [i, j]
            else: continue
    return None

def meet_condition(num1: int, num2: int, goal: int) -> bool: 
    """
    Verifies that both numbers are distinct and their sum is equal goal
    """
    return num1 != num2 and num1 + num2 == goal

print(find_first_sum([4, 5, 6, 2], 8))
print(find_first_sum([4, 6, 6, 2], 11))
