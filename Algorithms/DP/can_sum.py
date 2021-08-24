"""
Write a function that takes in a target sum and 
an array of numbers. Return whether or not it is
possible to generate the target sum using the
numbers in the array

Assume nonnegative, can use element as many times
i.e. can_sum(7, [5,3,4,7]) -> true

Reminder: branching factor ^ depth

m = target sum
n = numbers.length

Brute Force:
O(n^m) Time
O(m) Space

Memoization:
O(m*n) Time
O(m) Space

Tabulation:
O(m*n) Time
O(m) Space
"""

def can_sum(target, numbers, memo):
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False

    for num in numbers:
        remainder = target - num
        if can_sum(remainder, numbers, memo):
            memo[target] = True
            return True 

    memo[target] = False
    return False

def can_sum_tab(target, numbers):
    """
    Can make 0 out of current numbers.
    i.e. numbers = [3, 5]
    0 + 3 = 3 -> True
    0 + 5 = 5 -> True
    ...
    3 + 3 = 6 -> True
    3 + 5 = 8 -> True
    iterate until target + 1 (extra space for 0)
    """
    dp = [False for _ in range(target+1)]
    dp[0] = True

    for i in range(target+1):
        if dp[i]:
            for num in numbers:
                if i + num < target + 1:
                    dp[i + num] = True
    return dp[target]

def can_sum_fast(target, numbers):
    dp = [False for _ in range(target+1)]
    dp[0] = True
    for num in numbers:
        for i in range(num, target+1):
            dp[i] = dp[i] or dp[i-num]
    
    return dp[target]


print(can_sum(7, [5,3,4,7], {}))
print(can_sum(7, [2,3], {}))
print(can_sum(300, [7, 14], {}))

print(can_sum_tab(7, [5,3,4,7]))
print(can_sum_tab(7, [2,3]))
print(can_sum_tab(300, [7, 14]))

print(can_sum_fast(7, [5,3,4,7]))
print(can_sum_fast(7, [2,3]))
print(can_sum_fast(300, [7, 14]))