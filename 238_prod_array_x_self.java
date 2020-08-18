class Solution {
    /**
    Given an array nums of n integers where n > 1, 
    return an array output such that output[i] is equal 
    to the product of all the elements of nums except nums[i].

    Example:

    Input:  [1,2,3,4]
    Output: [24,12,8,6]
    Constraint: It's guaranteed that the product of the 
    elements of any prefix or suffix of the array 
    (including the whole array) fits in a 32 bit integer.

    Note: Please solve it without division and in O(n).
    **/
    public int[] productExceptSelf(int[] nums) {
        int[] out = new int[nums.length];
        out[0] = 1;
        for (int i = 1; i < nums.length; ++i) {
            out[i] = out[i-1] * nums[i-1];
        }
        int R = 1;
        for(int i = nums.length-1; i >= 0; --i) {
            out[i] = out[i] * R;
            R *= nums[i];
        }
        return out;
    }
}