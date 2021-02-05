"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

Chess is a two-player strategy board game played on a chessboard, which is a checkered gameboard with 64 squares arranged in an 8×8 grid. There are a few versions of game types that people play all over the world. In this design problem, we are going to focus on designing a two-player online chess game.

System Requirements
===================

The system should support two online players to play a game of chess.
All rules of international chess will be followed.
Each player will be randomly assigned a side, black or white.
Both players will play their moves one after the other. The white side plays the first move.
Players can’t cancel or roll back their moves.
The system should maintain a log of all moves by both players.
Each side will start with 8 pawns, 2 rooks, 2 bishops, 2 knights, 1 queen, and 1 king.
The game can finish either in a checkmate from one side, forfeit or stalemate (a draw), or resignation.

Actors:
=======
Player: A registered account in the system, who will play the game. The player will play chess moves.
Admin: To ban/modify players.

Here are the top use cases for chess:
======================================
Player moves a piece: To make a valid move of any chess piece.
Resign or forfeit a game: A player resigns from/forfeits the game.
Register new account/Cancel membership: To add a new member or cancel an existing member.
Update game log: To add a move to the game log.

"""


