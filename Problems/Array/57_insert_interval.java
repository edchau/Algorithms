/**
 * You are given an array of non-overlapping intervals intervals 
 * where intervals[i] = [starti, endi] represent the start and the end 
 * of the ith interval and intervals is sorted in ascending order by 
 * starti. You are also given an interval newInterval = [start, end] 
 * that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in 
ascending order by starti and intervals still does not have any overlapping 
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
 * 
 */

class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> result = new ArrayList<>();
        int index = 0;
        
        while (index < intervals.length && intervals[index][1] < newInterval[0]) {
            result.add(intervals[index]);
            index += 1;
        }
        
        while (index < intervals.length && intervals[index][0] <= newInterval[1]) {
            newInterval[0] = Math.min(intervals[index][0], newInterval[0]);
            newInterval[1] = Math.max(intervals[index][1], newInterval[1]);
            index += 1;
        }
        result.add(newInterval);
        
        while (index < intervals.length) {
            result.add(intervals[index]);
            index += 1;
        }
        
        return result.toArray(new int[result.size()][]);
    }
}