"""
Write a function that takes in a target sum and an 
array of numbers. Return an array containing the 
shortest combination of numbers that add up to
the target sum.

Break ties arbitrarily

Reminder: branching factor ^ depth

m = target sum
n = numbers.length

Brute Force:
O(n^m * m) Time
O(m) Space

Memoization:
O(n*m*m) Time
O(m*m) Space 

Tabulation:
O(n*m*m) Time
O(m*m) Space 
"""

def best_sum(target, numbers, memo):

    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None

    shortest_combination = None

    for num in numbers:
        remainder = target - num
        result = best_sum(remainder, numbers, memo)
        if result != None:
            combination = result + [num]

            if shortest_combination == None or len(combination) < len(shortest_combination):
                shortest_combination = combination
    
    memo[target] = shortest_combination
    return shortest_combination


def best_sum_tab(target, numbers):
    dp = [None for _ in range(target+1)]
    dp[0] = []

    for i in range(target+1):
        if dp[i] != None:
            for num in numbers:
                if i + num < target + 1:
                    """
                    compare length of dp[i] + 1 num to the current
                    dp[i+num] before updating dp
                    """
                    if dp[i+num] is None or len(dp[i]) + 1 < len(dp[i+num]):
                        dp[i+num] = dp[i] + [num]
    return dp[i]

print(best_sum(7, [5,3,4,7], {}))
print(best_sum(8, [2,3,5], {}))
print(best_sum(8, [1,4,5], {}))
print(best_sum(100, [1,2,5,25], {}))

print(best_sum_tab(7, [5,3,4,7]))
print(best_sum_tab(8, [2,3,5]))
print(best_sum_tab(8, [1,4,5]))
print(best_sum_tab(100, [1,2,5,25]))