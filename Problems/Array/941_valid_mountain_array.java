/**
Given an array of integers arr, return true if and only if it is 
a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
**/

class Solution {
    public boolean validMountainArray(int[] arr) {
        if (arr.length < 3) {
            return false;
        }
        int i = 0;
        while (i + 1 < arr.length && arr[i] < arr[i+1]) {
            ++i;
        }
        int j = arr.length - 1;
        while (j - 1 >= 0 && arr[j] < arr[j-1]) {
            --j;
        }
        return i > 0 && i == j && j < arr.length - 1;
    }
}