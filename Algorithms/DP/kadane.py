"""
Kadane's Algorithm

Used to find largest contiguous subarray sum

O(N) Time
O(1) Space
"""

test_input = [-2,1,-3,4,-1,2,1,-5,4]


def kadane(arr):
    if len(arr) == 0:
        return 0
    
    maxSum = arr[0]
    curr = arr[0]

    for i in arr:
        curr = max(i, curr + i)
        if curr > maxSum:
            maxSum = curr
    
    return maxSum

print(kadane(test_input))
