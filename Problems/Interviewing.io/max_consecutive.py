"""
Given a list of integers L, find the max length of
a sequence of consecutive numbers that can be formed
using elements from L
"""

# O(n) have two pointers and mark
# as visited so we dont traverse array again

def max_consecutive_sequence(arr):
    visited = set()
    max_length = 0
    arr = set(arr) # for constant time access
    for num in arr:
        if num not in visited:
            visited.add(num)
            length = 1
            next = num + 1
            while next in arr:
                visited.add(next)
                length += 1
                next += 1

            prev = num - 1
            while prev in arr:
                visited.add(prev)
                length += 1
                prev -= 1

        max_length = max(max_length, length)
    return max_length


L = [5, 2, 99, 3, 4, 1, 100]
# returns 5 -> (1, 2, 3, 4, 5)
print(max_consecutive_sequence(L))