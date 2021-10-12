"""
Given an array nums of integers, return the length of 
the longest arithmetic subsequence in nums.

Recall that a subsequence of an array nums is a list nums[i1], 
nums[i2], ..., nums[ik] with 0 <= i1 < i2 < ... < ik <= nums.length - 1, 
and that a sequence seq is arithmetic if seq[i+1] - seq[i] are all the 
same value (for 0 <= i < seq.length - 1).

 

Example 1:

Input: nums = [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
"""


import collections
class Solution(object):
    def longestArithSeqLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [collections.defaultdict(int) for _ in range(len(nums))]
        max_len = 0
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                # how many at point j do we have the current
                # diff, and add 1 to that
                dp[i][diff] = 1 + dp[j][diff]
                max_len = max(max_len, dp[i][diff])
            
        return max_len + 1

"""
class Solution {
    public int longestArithSeqLength(int[] nums) {
        int n = nums.length;
        int result = 0;
        HashMap<Integer, Integer>[] dp = new HashMap[n];
        
        for (int i = 0; i < nums.length; ++i) {
            dp[i] = new HashMap<>();
            for (int j = 0; j < i; ++j) {
                int diff = nums[i] - nums[j];
                dp[i].put(diff, dp[j].getOrDefault(diff, 1) + 1);
                result = Math.max(result, dp[i].get(diff));
            }
        }
        
        return result;
    }
}

"""