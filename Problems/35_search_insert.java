class Solution {
    /**
    35. Search Insert Position
    Given a sorted array and a target value, 
    return the index if the target is found. 
    If not, return the index where it would 
    be if it were inserted in order.

    You may assume no duplicates in the array.
    **/
    public int searchInsert(int[] nums, int target) {
        for(int i = 0; i < nums.length; ++i) {
            if (nums[i] == target) {
                return i;
            } else if (nums[i] > target) {
                return i == 0 ? 0 : i;
            }
        }
        return nums.length;
    }
}