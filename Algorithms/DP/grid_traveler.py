"""
Given m x n Grid, travel from top left square
to bottom right square (1,1)

i.e. grid_traveler(2,3) -> 3
idea: break down grid as you go

Reminder: branching factor ^ depth

Brute Force:
O(2^(n+m)) Time
O(n+m) Space

Memoization:
O(m*n) Time
O(m+n) Space

Tabulation:
O(m*n) Time
O(m*n) Space
"""

def grid_traveler(m, n, memo = {}):
    if (m,n) in memo:
        return memo[(m,n)]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0

    memo[(m,n)] = grid_traveler(m-1, n, memo) + grid_traveler(m, n-1, memo)
    return memo[(m,n)]

def grid_traveler_tab(m, n):
    """
    Can move right or down. Starting at (1,1), (1,2) will
    have have 1 way to move to from (1,1) and (2,1) will
    get 1 way. Then as we go to the next row, we see an 
    extra way to get to (2,2) is added from (2,1) 
    """
    db = [[0 for col in range(n+1)] for row in range(m+1)]
    db[1][1] = 1 # 1 way to travel in 1 x 1 grid

    for i in range(m + 1):
        for j in range(n + 1):
            cur = db[i][j]
            if j+1 < n+1:
                db[i][j+1] += cur
            if i+1 < m+1:
                db[i+1][j] += cur

    return db[m][n]

print(grid_traveler(1,1))
print(grid_traveler(2,3))
print(grid_traveler(3,2))
print(grid_traveler(3,3))
print(grid_traveler(18,18))

print(grid_traveler_tab(3,2))
print(grid_traveler_tab(18,18))