Leetcode Result:- https://leetcode.com/problems/valid-sudoku/submissions/1685195344

"""Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true"""

Code start
___________________________________
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                # Check row
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                # Check column
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                # Check box
                idx = (r // 3) * 3 + (c // 3)
                if val in boxes[idx]:
                    return False
                boxes[idx].add(val)
        
        return True
