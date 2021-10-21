/**
 * You are a professional robber planning to rob houses along a street. 
 * Each house has a certain amount of money stashed. All houses at this 
 * place are arranged in a circle. That means the first house is the neighbor 
 * of the last one. Meanwhile, adjacent houses have a security system connected, 
 * and it will automatically contact the police if two adjacent houses were broken 
 * into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
 * 
 */

class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        int[] memo = new int[nums.length + 1];
        Arrays.fill(memo, -1);
        int[] memo2 = new int[nums.length + 1];
        Arrays.fill(memo2, -1);
        return Math.max(maxRob(nums, 1, nums.length - 1, memo), maxRob(nums, 0, nums.length - 2, memo2));
    }
    
    public int maxRob(int[] nums, int end, int k, int[] memo) {
        if (k < end) {
            return 0;
        }
        
        if (memo[k] >= 0) {
            return memo[k];
        }
        
        int result = Math.max(nums[k] + maxRob(nums, end, k-2, memo), maxRob(nums, end, k-1, memo));
            
        memo[k] = result;
        return memo[k];
    }
}