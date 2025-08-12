'''
VALID SUDOKU

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
'''
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Initialize sets to track numbers in each row, column, and 3x3 box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        
        # Iterate through each cell in the 9x9 board
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    # Check if number already exists in current row
                    if num in rows[i]:
                        return False
                    rows[i].add(num)
                    
                    # Check if number already exists in current column
                    if num in cols[j]:
                        return False
                    cols[j].add(num)
                    
                    # Calculate the index of the 3x3 box
                    box_idx = (i // 3) * 3 + j // 3
                    if num in boxes[box_idx]:
                        return False
                    boxes[box_idx].add(num)
        
        return True
            