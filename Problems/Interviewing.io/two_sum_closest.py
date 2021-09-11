"""
Given an int array nums and an int target. Find two 
integers in nums such that the sum is closest to target.

Example 1:

Input: nums = [1, 2, 3, 4, 5], target = 10
Output: [4, 5]
Example 2:

Input: nums = [-1, 2, 1, -4], target = 4
Output: [2, 1]
"""
def two_sum_closest(nums, target):
    nums.sort()
    result = float('inf')
    left = 0
    right = len(nums)-1
    values = []

    while left < right:
        n_left = nums[left]
        n_right = nums[right]
        total = n_left + n_right

        if total <= target:
            left += 1
        elif total > target:
            right -= 1

        if abs(total - target) < abs(result - target):
            result = total
            if len(values) == 0:
                values.append(n_left)
                values.append(n_right)
            else:
                values[0] = n_left
                values[1] = n_right    
                
    return values



nums1 = [1, 2, 3, 4, 5]
target1 = 10
print(two_sum_closest(nums1, target1))
# Output: [4, 5]

nums2 = [-1, 2, 1, -4]
target2 = 4
print(two_sum_closest(nums2, target2))
# Output: [2, 1]