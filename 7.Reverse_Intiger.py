LeetCode Result:- https://leetcode.com/problems/reverse-integer/submissions/1685175076

"""Example 1:
Input: x = 123
Output: 321"""

Code starts
_____________________________
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        res = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check if res will overflow after appending digit
            if res > (INT_MAX - digit) / 10:
                return 0
            
            res = res * 10 + digit
        
        return sign * res
