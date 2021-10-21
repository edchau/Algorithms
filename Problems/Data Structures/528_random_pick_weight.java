/**
You are given a 0-indexed array of positive integers w where w[i] 
describes the weight of the ith index.

You need to implement the function pickIndex(), which randomly picks an 
index in the range [0, w.length - 1] (inclusive) and returns it. The 
probability of picking an index i is w[i] / sum(w).

For example, if w = [1, 3], the probability of picking index 0 is 
1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 
1 is 3 / (1 + 3) = 0.75 (i.e., 75%).
**/

class Solution {
    
    private Random rand = new Random();
    private int[] wSums;
    
    public Solution(int[] w) {
        
        // bins of diff prob
        for (int i = 1; i < w.length; ++i) {
            w[i] += w[i-1];
        }
        this.wSums = w;
    }
    
    public int pickIndex() {
        int len = wSums.length;
        int idx = rand.nextInt(wSums[len-1]) + 1;
        // int i = Arrays.binarySearch(wSums, idx);
        /**
         * Arrays.binarySearch() returns the index of the element 
         * if it's in the array or ( -(insertion point) - 1)
         */
        int left = 0, right = len - 1;
        // search position 
        while(left < right){
            int mid = left + (right-left)/2;
            if(wSums[mid] == idx)
                return mid;
            else if(wSums[mid] < idx)
                left = mid + 1;
            else
                right = mid;
        }
        // insertion point if not valid
        return left;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(w);
 * int param_1 = obj.pickIndex();
 */