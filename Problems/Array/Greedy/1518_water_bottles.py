"""
Given numBottles full water bottles, you can exchange numExchange 
empty water bottles for one full water bottle.

The operation of drinking a full water bottle turns it into an 
empty bottle.

Return the maximum number of water bottles you can drink.

"""
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        empty_bottles = 0
        result = 0
        while numBottles > 0:
            # add current number of full bottles
            result += numBottles
            # add on empty bottles
            numBottles += empty_bottles
            empty_bottles = 0
            # get remaining bottles that are empty
            remainder = numBottles % numExchange
            # exchange bottles
            numBottles //= numExchange
            # add remaining empty bottles to carry over
            # to next iteration
            empty_bottles += remainder
        return result