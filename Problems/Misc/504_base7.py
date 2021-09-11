class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        n, res = abs(num), ''
        
        while n:
            res = str(n % 7) + res
            n /= 7
            
        if num < 0:
            return '-' + res
        
        return res or "0"
