"""
You have n boxes. You are given a binary string boxes of length n, 
where boxes[i] is '0' if the ith box is empty, and '1' if it contains 
one ball.

In one operation, you can move one ball from a box to an adjacent box. 
Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, 
there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number 
of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.

"""
class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        output = [0] * len(boxes)
        
        left_count = 0
        right_count = 0
        left_cost = 0
        right_cost = 0
        
        # each turn, the left_count moves over 1 so we have
        # to update our total cost by shifting all our current
        # counts (number of 1's). If there is an extra 1 to our
        # left, then we increment the number of boxes we've seen
        # right to left
        for i in range(1, len(boxes)):
            # compare previous
            if boxes[i-1] == '1':
                left_count += 1
            left_cost += left_count
            # print(left_count, left_cost)
            output[i] += left_cost
        
        # left to right
        for i in range(len(boxes)-2, -1, -1):
            # compare previous
            if boxes[i+1] == '1':
                right_count += 1
            right_cost += right_count
            print(right_count, right_cost)
            output[i] += right_cost
        
        return output