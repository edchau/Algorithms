"""
Convex Hull Algorithm

Maximize Area while minimizing circumference

https://leetcode.com/problems/erect-the-fence/

https://leetcode.com/problems/erect-the-fence/discuss/1442266/A-Detailed-Explanation-with-Diagrams-(Graham-Scan)

https://www.youtube.com/watch?v=B2AJoQSZf4M&ab_channel=StableSort

O(nlogn) (sort)
"""

class Solution:
    def outerTrees(self, trees):
        # cross product to determine clockwise/cc
        # area is positive = counter clockwise
        def cmp(p1, p2, p3):
            x1, y1 = p1
            x2, y2 = p2            
            x3, y3 = p3
            
            return (y3-y2)*(x2-x1) - (y2-y1)*(x3-x2)
        
        points = sorted(trees)
        
        lower = []
        upper = []
        for point in points:
            while len(lower) >= 2 and cmp(lower[-2], lower[-1], point) > 0:
                lower.pop()
            while len(upper) >= 2 and cmp(upper[-2], upper[-1], point) < 0:
                upper.pop()
            
            lower.append(tuple(point))
            upper.append(tuple(point))
        
        return list(set(lower+upper))