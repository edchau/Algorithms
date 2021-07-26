class Solution {
    /**
     * Write a function to find the longest common prefix string amongst an array of strings.

        If there is no common prefix, return an empty string "".

        Example 1:

        Input: strs = ["flower","flow","flight"]
        Output: "fl"
        Example 2:

        Input: strs = ["dog","racecar","car"]
        Output: ""
        Explanation: There is no common prefix among the input strings.
     */ 
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }
        return divide(strs, 0, strs.length-1);
    }
    
    private String divide(String[] strs, int l, int r) {
        if (l == r) {
            return strs[l];
        } else {
            int mid = (l+r)/2;
            String left = divide(strs, l, mid);
            String right = divide(strs, mid+1, r);
            return conquer(left, right);
        }
    }
    
    private String conquer(String left, String right) {
        int min = Math.min(left.length(), right.length());
        for (int i = 0; i < min; ++i) {
            if (left.charAt(i) != right.charAt(i)) {
                return left.substring(0, i);
            }
        }
        return left.substring(0, min);
    }
}