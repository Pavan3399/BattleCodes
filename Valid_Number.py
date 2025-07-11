LeetCode Result:- https://leetcode.com/problems/valid-number/submissions/1693880758

Example 1:
Input: s = "0"
Output: true

Example 2:
Input: s = "e"
Output: false

Example 3:
Input: s = "."
Output: false

Code
________________________
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pattern = re.compile(r"""
            ^                           # start of string
            [\+\-]?                     # optional sign
            (
                (                       # decimal
                    (\d+\.\d*)          # digits + dot + optional digits
                    |                   # OR
                    (\.\d+)            # dot + digits
                )
                |                       # OR
                (\d+)                   # integer
            )
            ([eE][\+\-]?\d+)?           # optional exponent
            $                           # end of string
        """, re.VERBOSE)
        
        return pattern.match(s.strip()) is not None
