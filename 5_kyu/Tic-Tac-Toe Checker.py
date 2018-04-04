__author__ = 'mohan'

"""
If we were to set up a Tic-Tac-Toe game, we would want to know whether the board's current state is solved, wouldn't we? Our goal is to create a function that will check that for us!

Assume that the board comes in the form of a 3x3 array, where the value is 0 if a spot is empty, 1 if it is an "X", or 2 if it is an "O", like so:

[[0, 0, 1],
 [0, 1, 2],
 [2, 1, 0]]
We want our function to return:

-1 if the board is not yet finished (there are empty spots),
1 if "X" won,
2 if "O" won,
0 if it's a cat's game (i.e. a draw).
You may assume that the board passed in is valid in the context of a game of Tic-Tac-Toe.
"""

def isSolved(board):
    for row in board:
        if len(set(row)) == 1 and row[0]:
            return row[0]
    for col in zip(*board):
        if len(set(col)) == 1 and col[0]:
            return col[0]
    cross_left_to_right = []
    cross_right_to_left = []
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if i==j:
                cross_left_to_right.append(cell)
            if i+j == 2:
                cross_right_to_left.append(cell)
    if len(set(cross_left_to_right)) == 1 and cross_left_to_right[0]: return cross_left_to_right[0];
    if len(set(cross_right_to_left)) == 1 and cross_right_to_left[0]: return cross_right_to_left[0];
    if filter(lambda x: 0 in x, board):
        return -1
    else:
        return 0
    
# 1
# def isSolved(board):
#     for sign in [1, 2]:
#         win = [sign] * 3
#         if (win in board or
#             win in zip(*board[::-1]) or
#             win in [[board[x][0], board[1][1], board[2-x][2]] for x in [0, 2]]):
#                 return sign
#     return -1 if 0 in sum(board, []) else 0

board = [[0,0,2],
         [0,0,0],
         [1,0,1]]



# (0,0) (0,1) (0,2)

# (1,0) (1,1) (1,2)

# (2,0) (2,1) (2,2)


# print isSolved(board)