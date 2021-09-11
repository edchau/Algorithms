"""
At a lemonade stand, each lemonade costs $5. Customers are 
standing in a queue to buy from you, and order one at a time 
(in the order specified by bills). Each customer will only 
buy one lemonade and pay with either a $5, $10, or $20 bill. 
You must provide the correct change to each customer so that 
the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Given an integer array bills where bills[i] is the bill the 
ith customer pays, return true if you can provide every 
customer with correct change, or false otherwise.
"""

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        bank = {5: 0, 10: 0, 20: 0}
        
        for bill in bills:
            change = bill - 5
            
            if change == 5:
                if bank[5] > 0:
                    bank[5] -= 1
                else:
                    return False
            elif change == 15:
                if (bank[10] > 0 and bank[5] > 0):
                    bank[10] -= 1
                    bank[5] -= 1
                elif bank[5] > 2:
                    bank[5] -= 3
                else:
                    return False
            
            bank[bill] += 1
        
        return True