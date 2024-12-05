"""
Validate sudoku
input: board: list[list[char]]
board - list of rows (first arg is row, second is col)
'.' = blank
only if is valid at current state, not if solvable
"""

from typing import List, Generator


class Solution:
    digits = range(1, 10)
    blank = '.'
    def validateRows(self, board: List[List[str]]) -> bool:
        for row in board:
            for d in self.digits:
                if row.count(d) > 1:
                    return False
        return True


    def validateColumns(self, board: List[List[str]]) -> bool:
        for row_ind in range(9):
            found = set()
            for col_ind in range(9):
                d = board[row_ind][col_ind]
                if d in found and d is not self.blank:
                    return False
                found.add(d)
        return True

    def generateBoxIndex(self, box_number: int):
        row_offset = int((box_number % 3) * 3)
        col_offset = int((box_number // 3) * 3)

        for row in range(3):
            for col in range(3):
                yield(row + row_offset, col + col_offset)

    def validateBoxes(self, board: List[List[str]]) -> bool:
        for box_number in range(9):
            found = set()
            for row, col in self.generateBoxIndex(box_number):
                d = board[row][col]
                if d in found and d is not self.blank:
                    return False
                found.add(d)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.validateRows(board) \
            and self.validateColumns(board) \
            and self.validateBoxes(board)
