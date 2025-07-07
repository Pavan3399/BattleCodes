LeetCode Result:- https://leetcode.com/problems/spiral-matrix/submissions/1689599617

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Code
_____________________________
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # traverse from left to right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            
            # traverse downwards
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            if top <= bottom:
                # traverse from right to left
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                # traverse upwards
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        return res
