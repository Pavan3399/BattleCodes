Leetcode Result:- https://leetcode.com/problems/sudoku-solver/submissions/1685135985

"""Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]"""

"""Please go through step by step for better understanding"""
🔷 Idea
✅ We iterate through the board to find empty cells (denoted by .).
✅ For each empty cell, we try to place a digit 1..9 that satisfies:
Not already in the row.
Not already in the column.
Not already in the 3×3 box.
✅ Recursively try filling the next cells.
✅ If stuck → backtrack.

Code starts
________________________________________________________________________________________________
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Preprocess board to fill in sets and empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    box = (r // 3) * 3 + (c // 3)
                    boxes[box].add(val)

        def backtrack(index):
            if index == len(empty):
                return True

            r, c = empty[index]
            b = (r // 3) * 3 + (c // 3)

            for ch in '123456789':
                if ch not in rows[r] and ch not in cols[c] and ch not in boxes[b]:
                    board[r][c] = ch
                    rows[r].add(ch)
                    cols[c].add(ch)
                    boxes[b].add(ch)

                    if backtrack(index + 1):
                        return True

                    # undo
                    board[r][c] = '.'
                    rows[r].remove(ch)
                    cols[c].remove(ch)
                    boxes[b].remove(ch)

            return False

        backtrack(0)
