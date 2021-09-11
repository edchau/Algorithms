"""
https://www.youtube.com/watch?v=clqZGxkL3CA&t=1890s
Leetcode #11
"""

# Greedy Approach O(n)
# Have 2 pointers at end and beginning
# Then move minimum pointer 

def max_water_well(arr):

    left = 0
    right = len(arr)-1
    max_water = 0

    while left < right:
        distance = right - left
        water = 0
        if arr[left] < arr[right]:
            water = distance * arr[left]
            left += 1
        else:
            water = distance * arr[right]
            right -= 1

        max_water = max(max_water, water)

    return max_water

input = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_water_well(input))
