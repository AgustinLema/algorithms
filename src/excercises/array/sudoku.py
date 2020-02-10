from typings import List

>
class Solution:
    """
    Given a 2d array representing a sudoku board, determine if it is valid
    The array will contain numbers from 0 to 9 and also "." for empty spaces that shouldn't be validated
    Rules are not having repeated digits in columns, rows or in 3x3 squares.
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.validate_rows(board) and self.validate_columns(board) and self.validate_squares(board)
    
    def validate_rows(self, board):
        for y in range(len(board)):
            seen = set()
            for x in range(len(board[0])):
                if board[y][x] == '.': continue
                if board[y][x] in seen:
                    return False
                else:
                    seen.add(board[y][x])
        return True


    def validate_columns(self, board):
        for x in range(len(board[0])):
            seen = set()
            for y in range(len(board)):
                if board[y][x] == '.': continue
                if board[y][x] in seen:
                    return False
                else:
                    seen.add(board[y][x])
        return True


    def validate_squares(self, board):
        for vsq in range(3):
            for hsq in range(3):
                seen = set()
                for y_delta in range(3):
                    for x_delta in range(3):
                        y, x = x_delta + (hsq*3), y_delta + (vsq*3)
                        if board[y][x] == '.': continue
                        if board[y][x] in seen:
                            return False
                        else:
                            seen.add(board[y][x])
        return True
