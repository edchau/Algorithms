"""
Given an integer array nums and two integers left and right, 
return the number of contiguous nonempty subarrays in the range
left <= max array val <= right

i.e. [2, 1, 4, 3] left = 2 right = 3
output: 3

[2], [2,1], [3]

https://www.youtube.com/watch?v=FVzlY9cm-A0
"""


def count_subarray(nums, left, right):
    count = 0
    for i in range(len(nums)):
        max_num = nums[i]
        for j in range(i, -1, -1):
            max_num = max(max_num, nums[j])
            if max_num >= left and max_num <= right:
                count += 1
    return count

test_input = [2,1,4,3]
print(count_subarray(test_input, 2, 3))
test_input2 = [2,5,2,1,4,3]
print(count_subarray(test_input2, 2, 3))