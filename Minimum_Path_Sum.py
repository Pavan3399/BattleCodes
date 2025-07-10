LeetCode Result:- https://leetcode.com/problems/minimum-path-sum/submissions/1692608145

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12

COde
_____________________________
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        # fill the first row
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]
        
        # fill the first column
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        # fill the rest
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[m-1][n-1]
