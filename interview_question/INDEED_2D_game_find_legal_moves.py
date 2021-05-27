"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

We are designing a 2D game and we have a game map that we represent by an integer matrix.
For now, each cell can be a wall (denoted by -1) or a blank space (0).

# The player can move 1 space at a time up, down, left, or right.
The player can't go through walls or land on a wall, or go through the edges of the board.

# Write a function that, given a board and a player starting position (represented as a row-column pair),
returns all of the possible next positions for the player.

# n: width of the input board
# m: height of the input board

# Sample inputs (board, starting_position) and outputs (in any order):

# findLegalMoves(board, (1, 1)) =>
#   (0, 1), (1, 0)

# findLegalMoves(board, (5, 3)) =>
#   (5, 2), (5, 4), (4, 3), (6, 3)

# findLegalMoves(board, (5, 1)) =>
#   (6, 1), (4, 1), (5, 0), (5, 2)

# findLegalMoves(board, (6, 0)) =>
#   (5, 0), (6, 1)

# findLegalMoves(board, (6, 4)) =>
#   (5, 4), (6, 3)

# findLegalMoves(board, (0, 0)) =>
#   (0, 1), (1, 0)

# findLegalMoves(board, (2, 2)) =>
#   [empty]

"""

board = [
    [0, 0, 0, -1, -1],
    [0, 0, -1, 0, 0],
    [0, -1, 0, -1, 0],
    [0, 0, -1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]


def findLegalMoves(board, t):
    x, y = t
    p1 = x + 1, y
    p2 = x - 1, y
    p3 = x, y + 1
    p4 = x, y - 1

    pp = [p1, p2, p3, p4]

    for x, y in pp:
        if x >= len(board) or y >= len(board[0]) or x < 0 or y < 0 or -1 == board[x][y]:
            pp.remove((x, y))

    return pp


print(findLegalMoves(board, (6, 0)))

test_data = [
    ((1, 1), [(0, 1), (1, 0)]),
    ((5, 3), [(5, 2), (5, 4), (4, 3), (6, 3)]),
    ((5, 1), [(6, 1), (4, 1), (5, 0), (5, 2)]),
    ((6, 0), [(5, 0), (6, 1)]),
    ((6, 4), [(5, 4), (6, 3)]),
    ((0, 0), [(0, 1), (1, 0)]),
    ((2, 2), [])
]

for given, expected in test_data:
    print(f" Testing with given {given} and expected = {expected}")
    actual = findLegalMoves(board, given)
    print(f"actual value: {actual}")
    assert actual.sort() == expected.sort()
