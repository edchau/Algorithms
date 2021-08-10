"""
Calculate nth number in fibonacci sequence

Brute Force:
O(2^n) Time
O(n) Space

Memoization:
O(n) Time
O(n) Space

Tabulation:
O(n) Time
O(n) Space
"""

def fib(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

def fib_tab(n):
    db = [0 for _ in range(n+1)]
    db[1] = 1 
    for i in range(2, n+1):
        db[i] = db[i-1] + db[i-2]
    return db[n]


print(fib(50))
print(fib_tab(6))
print(fib_tab(50))