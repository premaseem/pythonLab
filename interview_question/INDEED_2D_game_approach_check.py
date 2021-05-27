"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

We are designing a 2D game and we have a game map that we represent by an integer matrix.
For now, each cell can be a wall (denoted by -1) or a blank space (0).

# The player can move 1 space at a time up, down, left, or right.
The player can't go through walls or land on a wall, or go through the edges of the board.

# Given a board and an end position for the player,
write a function to determine if it is possible to travel from every open cell on the board to the given end position.

# n: width of the input board
# m: height of the input board

# Sample inputs (board, starting_position) and outputs Boolean:

# Expected output:

# isReachable(board1, end1) -> True
# isReachable(board1, end2) -> True
# isReachable(board2, end1) -> False
# isReachable(board2, end2) -> False
# isReachable(board3, end1) -> False
# isReachable(board4, end1) -> True
# isReachable(board5, end1) -> True

"""



board = [
  [0,  0,  0, -1, -1],
  [0,  0, -1,  0,  0],
  [0, -1,  0, -1,  0],
  [0,  0, -1,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
  [0,  0,  0,  0,  0],
]


