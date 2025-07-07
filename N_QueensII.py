LeetCode Result:- https://leetcode.com/problems/n-queens-ii/submissions/1689556776

Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:
Input: n = 1
Output: 1

Code
____________________________
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        
        def backtrack(row, cols, diagonals1, diagonals2):
            if row == n:
                self.count += 1
                return
            for col in range(n):
                if col in cols or (row - col) in diagonals1 or (row + col) in diagonals2:
                    continue
                cols.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)
                
                backtrack(row + 1, cols, diagonals1, diagonals2)
                
                cols.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)
        
        backtrack(0, set(), set(), set())
        return self.count
