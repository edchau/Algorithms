"""
Write a function that takes in a target sum and
array as numbers. Return an array containing any
combination of elements that add up to exactly the
target sum, otherwise return none.

Break ties arbitrarily

Reminder: branching factor ^ depth

Brute Force:
O(n^m * m) Time
O(m) Space

Memoization:
O(n*m*m) Time
O(m*m) Space (max array length in memo is m)

Tabulation:
O(m^2*n) Time
O(m^2) Space 
"""

def how_sum(target, numbers, memo):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    for num in numbers:
        remainder = target - num
        result = how_sum(remainder, numbers, memo)
        if result != None:
            memo[target] = result + [num]
            return memo[target]

    memo[target] = None
    return None


def how_sum_tab(target, numbers):
    db = [None for _ in range(target+1)]
    db[0] = []

    for i in range(target+1):
        if db[i] != None:
            for num in numbers:
                if i + num < target + 1:
                    db[i+num] = db[i] + [num]
    return db[i]

print(how_sum(7, [5,3,4,7], {}))
print(how_sum(7, [2,3], {}))
print(how_sum(7, [2,4], {}))
print(how_sum(8, [2,3,5], {}))
print(how_sum(300, [7, 14], {}))

print(how_sum_tab(7, [5,3,4,7]))
print(how_sum_tab(7, [2,3]))
print(how_sum_tab(7, [2,4]))
print(how_sum_tab(8, [2,3,5]))
print(how_sum_tab(300, [7, 14]))