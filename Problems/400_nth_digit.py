"""
Given an integer n, return the nth digit of the infinite 
integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

Example 1:

Input: n = 3
Output: 3
Example 2:

Input: n = 11
Output: 0
Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
which is part of the number 10.
"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_digits = 1
        total_digits = 9
        """
        9 nums with 1 digit, 90 nums with 2 digits,
        900 nums with 3 digits...
        """
        while n - num_digits * total_digits > 0:
            n -= num_digits * total_digits
            total_digits *= 10
            num_digits += 1
            
        # Note: math.floor(math.log10(num) + 1) gives num digits
        """
        Calculate exact number given remaining digits
        """
        index = n % num_digits
        num = pow(10, num_digits - 1)
        if index == 0:
            # 0th digit of a number means the one before
            num += n // num_digits - 1
        else:
            num += n // num_digits
            
        """
        Find digit in num
        """
        if index != 0:
            diff = num_digits - index
            for _ in range(diff):
                num /= 10
        return num % 10
        