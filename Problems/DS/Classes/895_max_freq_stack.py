"""
Design a stack-like data structure to push elements to the stack and 
pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the 
stack's top is removed and returned.
"""
import collections
class FreqStack(object):

    def __init__(self):
        self.freq = collections.defaultdict(int)
        self.nums = collections.defaultdict(list)
        self.max_freq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.freq[val] += 1
        self.max_freq = max(self.max_freq, self.freq[val])
        self.nums[self.freq[val]].append(val)
        

    def pop(self):
        """
        :rtype: int
        """
        val = self.nums[self.max_freq].pop()
        if len(self.nums[self.max_freq]) == 0:
            self.max_freq -= 1
        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()