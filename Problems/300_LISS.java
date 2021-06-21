class Solution {
    /**
        Given an integer array nums, return the length of the longest 
        strictly increasing subsequence.

        A subsequence is a sequence that can be derived from an array 
        by deleting some or no elements without changing the order of 
        the remaining elements. For example, [3,6,2,7] is a subsequence
         of the array [0,3,1,6,2,2,7].
     */
    public int lengthOfLIS(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        int[] dp = new int[nums.length];
        int length = 1;
        dp[0] = 1;
        for (int i = 1; i < nums.length; ++i) {
            int maxVal = 0;
            for (int j = 0; j < i; ++j) {
                if(nums[i] > nums[j]) {
                    maxVal = Math.max(maxVal, dp[j]);
                }
            }
            dp[i] = maxVal + 1;
            length = Math.max(length, dp[i]);
        }
        return length;
    }
}