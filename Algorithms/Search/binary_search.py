"""
Binary Search Algorithm
O(logn)
"""


test_input = [1, 3, 4, 5, 6, 6, 6, 9, 10, 12, 15, 20]


def binary_search(lst, target):
    """
    Returns index where target occurs in lst
    """
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid
        
        elif lst[mid] > target:
            right = mid - 1

        elif lst[mid] < target:
            left = mid + 1
        
    # not present
    return -1


print(binary_search(test_input, 6))
print(binary_search(test_input, 9))
print(binary_search(test_input, 1))
print(binary_search(test_input, 20))
print(binary_search(test_input, 21))
print(binary_search(test_input, 2))