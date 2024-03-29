/**
 * You are a professional robber planning to rob houses along a street. 
 * Each house has a certain amount of money stashed, the only constraint 
 * stopping you from robbing each of them is that adjacent houses have 
 * security systems connected and it will automatically contact the police 
 * if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.
 * 
 */

class Solution {
    public int rob(int[] nums) {
        int[] memo = new int[nums.length + 1];
        Arrays.fill(memo, -1);
        return maxRob(nums, nums.length - 1, memo);
    }
    
    public int maxRob(int[] nums, int k, int[] memo) {
        if (k < 0) {
            return 0;
        }
        
        if (memo[k] >= 0) {
            return memo[k];
        }
        
        int result = Math.max(nums[k] + maxRob(nums, k-2, memo), maxRob(nums, k-1, memo));
            
        memo[k] = result;
        return memo[k];
    }
}