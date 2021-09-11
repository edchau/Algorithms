"""
You are given a 0-indexed binary string s and two integers minJump and 
maxJump. In the beginning, you are standing at index 0, which is equal 
to '0'. You can move from index i to index j if the following conditions 
are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

"""

class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        if s[len(s)-1] != '0':
            return False
        
        dp = [False for _ in range(len(s))]
        dp[0] = True
        
        prev_jump = 0
        
        # knapsack too slow so use
        # sliding window
        # prev jump counts if we're able
        # to jump to that location
        for i in range(1, len(s)):
            # anywhere within range, we can jump to
            # once we pass the initial window, 
            # we treat it like a knapsack problem
            if i >= minJump and dp[i-minJump]:
                prev_jump += 1
            
            """
            keeping sliding window with size equal to max - min, and as 
            we are moving we are increasing pre if incoming element is 
            true and decreasing it if outgoing element (last element of 
            window which was part of window earlier but now move out) was true.
            """
            if i > maxJump and dp[i-maxJump-1]:
                prev_jump -= 1
                
            if s[i] == '0' and prev_jump > 0:
                dp[i] = True
        
        return dp[len(s)-1]
    
    
    