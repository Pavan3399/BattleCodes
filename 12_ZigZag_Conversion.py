Leetcode Result:- https://leetcode.com/problems/zigzag-conversion/submissions/1685171592

"""Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"""

Code starts
_______________________________
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Create a list for each row
        rows = [''] * numRows
        current_row = 0
        going_down = False
        
        for c in s:
            rows[current_row] += c
            
            # Change direction at top or bottom
            if current_row == 0 or current_row == numRows - 1:
                going_down = not going_down
            
            current_row += 1 if going_down else -1
        
        # Concatenate all rows
        return ''.join(rows)
