"""
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the 
non-overlapping intervals that cover all the intervals in the input.


"""

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort(key = lambda x: x[0])
            
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            # if current start is less than the previous end
            if intervals[i][0] <= merged[-1][1]:
                merged[-1][1] = max(intervals[i][1], merged[-1][1])
            else:
                merged.append(intervals[i])
            
        return merged

"""
class Solution {
    public int[][] merge(int[][] intervals) {
        
        if (intervals.length <= 1) {
            return intervals;
        }
        
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        
        List<int[]> result = new ArrayList<>();
		int[] newInterval = intervals[0];
		result.add(newInterval);
        
        for (int[] i : intervals) {
            if (i[0] <= newInterval[1]) {
                newInterval[1] = Math.max(newInterval[1], i[1]);
            } else {
                newInterval = i;
                result.add(newInterval);
            }
        }
        
        return result.toArray(new int[result.size()][]);
    }
}
"""