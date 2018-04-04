__author__ = 'mohan'

"""
Sudoku Background
Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)

Sudoku Solution Validator
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
"""

def validSolution(board):
    sum_of_rows = [sum(row) for row in board if set(row) == set(range(1,10))]
    sum_of_cols = [sum(col) for col in zip(*board) if set(col) == set(range(1,10))]
    sum_of_subgrid = []
    grp1, grp2, grp3 = [], [], []
    for i, row in enumerate(board):
        grp1.extend(row[:3])
        grp2.extend(row[3:6])
        grp3.extend(row[6:])
        if (i+1) % 3 ==0:
            sum_of_subgrid.append(sum(grp1))
            sum_of_subgrid.append(sum(grp2))
            sum_of_subgrid.append(sum(grp3))
            grp1, grp2, grp3 = [], [], []
    return sum_of_rows == sum_of_cols == sum_of_subgrid


# def validSolution(board):
#     blocks = [[board[x+a][y+b] for a in (0, 1, 2) for b in (0, 1, 2)] for x in (0, 3, 6) for y in (0, 3, 6)]
#     return not filter(lambda x: set(x) != set(range(1, 10)), board + zip(*board) + blocks)


print validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                     [6, 7, 2, 1, 9, 5, 3, 4, 8],
                     [1, 9, 8, 3, 4, 2, 5, 6, 7],
                     [8, 5, 9, 7, 6, 1, 4, 2, 3],
                     [4, 2, 6, 8, 5, 3, 7, 9, 1],
                     [7, 1, 3, 9, 2, 4, 8, 5, 6],
                     [9, 6, 1, 5, 3, 7, 2, 8, 4],
                     [2, 8, 7, 4, 1, 9, 6, 3, 5],
                     [3, 4, 5, 2, 8, 6, 1, 7, 9]])