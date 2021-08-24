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
    dp = [None for _ in range(target+1)]
    dp[0] = []

    for i in range(target+1):
        if dp[i] != None:
            for num in numbers:
                if i + num < target + 1:
                    dp[i+num] = dp[i] + [num]
    return dp[target]

def how_sum_fast(target, numbers):
    dp = [None for _ in range(target+1)]
    dp[0] = []

    for num in numbers:
        for i in range(num, target+1):
            if i - num >= 0 and dp[i-num] != None:
                dp[i] = dp[i-num] + [num]

    return dp[target]

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

print(how_sum_fast(7, [5,3,4,7]))
print(how_sum_fast(7, [2,3]))
print(how_sum_fast(7, [2,4]))
print(how_sum_fast(8, [2,3,5]))
print(how_sum_fast(300, [7, 14]))