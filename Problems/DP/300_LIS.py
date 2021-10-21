"""
Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly 
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting 
some or no elements without changing the order of the remaining elements. 
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].


i.e.
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], 
therefore the length is 4.

O(nlogn) Time

Use Patience Sorting
"""

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1

        return max(dp)
        
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        stack = [nums[0]]
        
        for num in nums:
            for i in range(len(stack)):
                if stack[i] >= num:
                    stack[i] = num
                    break
            if num not in stack:
                stack.append(num)
        
        return len(stack)


"""
class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] memo = new int[nums.length];
        Arrays.fill(memo, 1);
        
        int longest = 1;
        for (int i = 1; i < nums.length; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[j] < nums[i]) {
                    memo[i] = Math.max(memo[i], memo[j] + 1);
                    longest = Math.max(longest, memo[i]);
                }
            }
        }
        return longest;
    }
    
}
"""