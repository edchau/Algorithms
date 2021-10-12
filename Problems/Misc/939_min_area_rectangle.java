/**
 * You are given an array of points in the X-Y plane points where 
 * points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, 
with sides parallel to the X and Y axes. If there is not any such 
rectangle, return 0.
 * 
 */

class Solution {
    public int minAreaRect(int[][] points) {
        HashMap<Integer, Set<Integer>> m = new HashMap<>();
        
        // We want to find diagonols instead of the same
        // side length to get the area of the rectangle
        for (int[] p : points) {
            if (!m.containsKey(p[0])) {
                m.put(p[0], new HashSet<>());
            }
            // store x values to possible y points
            m.get(p[0]).add(p[1]);
        }
        
        int minArea = Integer.MAX_VALUE;
        for(int[] p1 : points) {
            for(int[] p2 : points) {
                // skip points along same line
                if (p1[0] == p2[0] || p1[1] == p2[1]) {
                    continue;
                }
                if (m.get(p1[0]).contains(p2[1]) && m.get(p2[0]).contains(p1[1])) {
                    minArea = Math.min(minArea, Math.abs(p1[0] - p2[0]) * Math.abs(p1[1] - p2[1]));
                }
            }
        }
        
        if (minArea == Integer.MAX_VALUE) {
            return 0;
        }
        
        return minArea;
        
    }
}