LeetCode Result:- https://leetcode.com/problems/spiral-matrix-ii/submissions/1691484574

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:
Input: n = 1
Output: [[1]]

Code
_______________________________
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        num = 1
        
        while left <= right and top <= bottom:
            # top row
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1
            
            # right column
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            # bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1
            
            # left column
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
        
        return matrix
