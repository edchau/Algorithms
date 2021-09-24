"""
You are given an integer array nums. Two players are playing 
a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. 
Both players start the game with a score of 0. At each turn, the 
player takes one of the numbers from either end of the array (i.e., 
nums[0] or nums[nums.length - 1]) which reduces the size of the array 
by 1. The player adds the chosen number to their score. The game ends 
when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both 
players are equal, then player 1 is still the winner, and you should 
also return true. You may assume that both players are playing optimally.


note: same problem as https://leetcode.com/problems/stone-game/

"""
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # difference between players
        # p1, p2 are pointers to front and end
        # chooses whichever one is greater score
        return self.score(0, len(nums)-1, nums, {}) >= 0
    
    def score(self, p1, p2, nums, memo):
        key = (p1, p2)
        if key in memo:
            return memo[key]
        
        if p1 == p2:
            return nums[p1]
        
        # - causes it to alternate so player 2 will subtract from score
        memo[key] = max(nums[p1]-self.score(p1+1, p2, nums, memo), nums[p2]-self.score(p1, p2-1, nums, memo))
        return memo[key]