"""Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3."""

"""Please go thorugh Step by Step for better understanding"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        Divide two integers without using multiplication, division and mod operator.
        Truncate toward zero. Clamp result to 32-bit signed integer range.
        
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Handle overflow
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Special case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine sign of result
        negative = (dividend < 0) != (divisor < 0)
        
        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        result = 0
        
        # Subtract multiples of divisor
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            # Double the divisor until it's just smaller than dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            # Subtract and add to result
            dividend -= temp
            result += multiple
