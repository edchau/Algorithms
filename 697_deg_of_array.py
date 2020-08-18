class Solution:
    """
    697. Degree of an Array
    Given a non-empty array of non-negative integers nums, 
    the degree of this array is defined as the maximum frequency 
    of any one of its elements.

    Your task is to find the smallest possible length of a 
    (contiguous) subarray of nums, that has the same degree as nums.

    Input: [1, 2, 2, 3, 1]
    Output: 2
    Explanation: 
    The input array has a degree of 2 because both elements 1 and 2 appear twice.
    Of the subarrays that have the same degree:
    [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
    The shortest length is 2. So return 2.
    """
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for ind, x in enumerate(nums):
            if x not in left:
                left[x] = ind
            right[x] = ind
            count[x] = count.get(x, 0) + 1
        
        ans = len(nums)
        deg = max(count.values())
        for x in count:
            if count[x] == deg:
                ans = min(ans, right[x] - left[x] + 1)
        return ans