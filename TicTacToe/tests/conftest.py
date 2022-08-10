
# flake8: noqa
import sys
import pytest

sys.path.append('C:/Users/Dell/python_projects')  # noqa

from TicTacToe.constants import DRAW, EMPTY, PLAYERO, PLAYERX  # noqa

# Create test boards
board_1 = [
    [EMPTY, PLAYERX, PLAYERO],
    [PLAYERX, PLAYERX, EMPTY],
    [PLAYERO, EMPTY, PLAYERO],
]
score_1 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
result_1 = [
    [0, 0, 0],
    [3, 0, -5],
    [0, 5, 0],
]
expected_1 = (2, 1)


board_2 = [
    [PLAYERO, PLAYERX, PLAYERX],
    [PLAYERO, PLAYERX, EMPTY],
    [PLAYERO, EMPTY, PLAYERO],
]
score_2 = [
    [1.0, -1.0, -1.0],
    [1.0, -1.0, -1.0],
    [1.0, -1.0, 1.0],
]
result_2 = [
    [0, 13, 0],
    [-1, 0, 9],
    [20, 8, 0],
]
expected_2 = (1, 2)


board_3 = [
    [EMPTY, PLAYERX, PLAYERO],
    [PLAYERO, PLAYERX, EMPTY],
    [PLAYERX, PLAYERO, PLAYERO],
]

board_4 = [
    [PLAYERO, PLAYERX, PLAYERO, PLAYERX],
    [EMPTY, PLAYERX, EMPTY, PLAYERO],
    [PLAYERO, EMPTY, PLAYERO, PLAYERX],
]

board_5 = [
    [PLAYERO, PLAYERX, PLAYERO, PLAYERX],
    [EMPTY, PLAYERX, EMPTY, PLAYERO],
    [PLAYERO, EMPTY, PLAYERO, PLAYERX],
    [PLAYERX, EMPTY, EMPTY, PLAYERX],
    [PLAYERO, PLAYERX, PLAYERO, PLAYERX],
]
score_5 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
result_5 = [
    [0, 0, 0, 0, 0],
    [-10, 0, 10, 0, 0],
    [0, 20, 0, 0, 50],
    [0, 9, 40, 0, 0],
    [90, 0, 0, -10, 0],
]
expected_5 = (3, 2)


# Win style boards
win_board_1 = [
    [EMPTY, PLAYERX, PLAYERO],
    [PLAYERO, PLAYERX, EMPTY],
    [PLAYERX, PLAYERX, PLAYERO],
]

win_board_2 = [
    [PLAYERO, PLAYERX, PLAYERO],
    [PLAYERO, PLAYERO, PLAYERX],
    [PLAYERX, PLAYERX, PLAYERO],
]

win_board_3 = [
    [PLAYERO, PLAYERX, PLAYERO, PLAYERX],
    [PLAYERO, PLAYERO, PLAYERX, EMPTY],
    [PLAYERX, PLAYERX, PLAYERO, EMPTY],
    [PLAYERX, PLAYERX, PLAYERO, EMPTY],
]

win_board_4 = [
    [PLAYERX, PLAYERX, PLAYERO, PLAYERX],
    [PLAYERO, PLAYERO, PLAYERO, PLAYERO],
    [PLAYERX, PLAYERX, PLAYERX, EMPTY],
]

win_board_5 = [
    [PLAYERX, PLAYERX, PLAYERO, PLAYERX],
    [PLAYERO, PLAYERO, PLAYERX, PLAYERO],
    [PLAYERX, PLAYERX, PLAYERX, PLAYERO],
]
