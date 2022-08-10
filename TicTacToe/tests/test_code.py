# flake8: noqa

from copy import deepcopy
import sys
from TicTacToe import poc_ttt_provided as provided
import pytest

sys.path.append('C:/Users/Dell/python_projects')
from TicTacToe.code import (
    NTRIALS, SCORE_CURRENT, SCORE_OTHER, add_score,
    get_score_to_add, mc_move, mc_trial,
    mc_update_scores, init_empty_scores,
    get_best_move
)
from TicTacToe.constants import (
    DIAG_X, DIAG_Y, DOWN, DRAW,
    EMPTY, PLAYERO, PLAYERX, RIGHT
)
from TicTacToe.poc_ttt_provided import TTTBoard, switch_player
from TicTacToe.poc_ttt_provided import get_board_dim

from conftest import (
    board_1, board_2, board_3, board_4, board_5,
    win_board_1, win_board_2, win_board_3, win_board_4,
    win_board_5, score_1, score_2, result_1, result_2,
    expected_1, expected_2, score_5, result_5, expected_5
)


@pytest.mark.parametrize("input_1, input_2, output", [
    (PLAYERO, PLAYERO, SCORE_CURRENT),
    (PLAYERO, PLAYERX, SCORE_OTHER),
    (PLAYERX, PLAYERO, SCORE_OTHER),
    (PLAYERX, PLAYERX, SCORE_CURRENT),
])
def test_add_score(input_1, input_2, output):
    computed = add_score(input_1, input_2)
    assert computed == output


@pytest.mark.parametrize("input_1, input_2, input_3, output", [
    (PLAYERO, PLAYERO, PLAYERO, SCORE_CURRENT),
    (PLAYERO, PLAYERX, PLAYERO, -SCORE_CURRENT),
    (PLAYERO, PLAYERO, PLAYERX, -SCORE_OTHER),
    (PLAYERO, PLAYERX, PLAYERX, SCORE_OTHER),
    (PLAYERX, PLAYERX, PLAYERX, SCORE_CURRENT),
    (PLAYERX, PLAYERO, PLAYERO, SCORE_OTHER),
    (PLAYERX, PLAYERO, PLAYERX, -SCORE_CURRENT),
    (PLAYERX, PLAYERX, PLAYERO, -SCORE_OTHER),
])
def test_get_score_to_add(input_1, input_2, input_3, output):
    computed = get_score_to_add(input_1, input_2, input_3)
    assert computed == output


@pytest.mark.parametrize(
    "board, dim",
    [
        (board_1, (3, 3)),
        (board_2, (3, 3)),
        (board_3, (3, 3)),
        (board_4, (3, 4)),
        (board_5, (5, 4)),
    ]
)
def test_get_board_dim(board, dim):
    assert get_board_dim(board) == dim


def test_board_create():
    board = TTTBoard(dim=(4, 3))
    assert board._dim == (4, 3)
    assert get_board_dim(board._board) == (4, 3)


@pytest.mark.parametrize(
    "board, dim",
    [
        (board_1, (3, 3)),
        (board_2, (3, 3)),
        (board_3, (3, 3)),
        (board_4, (3, 4)),
        (board_5, (5, 4)),
    ]
)
def test_board_get_dim(board, dim):
    board = TTTBoard(board=board)
    assert board.get_dim() == dim


@pytest.mark.parametrize(
    "board, value",
    [
        (board_1, True),
        (board_2, True),
        (board_3, True),
        (board_4, False),
        (board_5, False),
    ]
)
def test_board_is_square(board, value):
    board = TTTBoard(board=board)
    assert board.is_square() == value


@pytest.mark.parametrize(
    "board, value",
    [
        (board_1, 3),
        (board_2, 3),
        (board_3, 3),
        (board_4, 3),
        (board_5, 5),
    ]
)
def test_board_get_height(board, value):
    board = TTTBoard(board=board)
    assert board.get_height() == value


@pytest.mark.parametrize(
    "board, value",
    [
        (board_1, 3),
        (board_2, 3),
        (board_3, 3),
        (board_4, 4),
        (board_5, 4),
    ]
)
def test_board_get_width(board, value):
    board = TTTBoard(board=board)
    assert board.get_width() == value


@pytest.mark.parametrize(
    "board, cell, value",
    [
        (board_1, (0, 0), EMPTY),
        (board_2, (2, 2), PLAYERO),
        (board_3, (1, 0), PLAYERO),
        (board_4, (2, 3), PLAYERX),
        (board_5, (4, 2), PLAYERO),
    ]
)
def test_board_square(board, cell, value):
    board = TTTBoard(board=board)
    assert board.square(*cell) == value


@pytest.mark.parametrize(
    "board, expected",
    [
        (board_1, [(0, 0), (2, 1), (1, 2)]),
        (board_2, [(2, 1), (1, 2)]),
        (board_3, [(0, 0), (1, 2)]),
        (board_4, [(1, 0), (1, 2), (2, 1)]),
        (board_5, [(1, 0), (1, 2), (2, 1), (3, 1), (3, 2)]),
    ]
)
def test_get_empty_squares(board, expected):
    board = TTTBoard(board=board)
    computed = board.get_empty_squares()
    computed.sort()
    expected.sort()
    assert computed == expected


@pytest.mark.parametrize(
    "board, cell, value, expected",
    [
        (board_1, (0, 0), PLAYERO, [(2, 1), (1, 2)]),
        (board_2, (1, 2), PLAYERX, [(2, 1)]),
        (board_3, (0, 0), PLAYERO, [(1, 2)]),
        (board_4, (2, 1), PLAYERX, [(1, 0), (1, 2)]),
        (board_5, (3, 2), PLAYERO, [(1, 0), (1, 2), (2, 1), (3, 1)]),
    ]
)
def test_remove_empty_square(board, cell, value, expected):
    board = TTTBoard(board=board)
    board.move(*cell, value)
    assert board._board[cell[0]][cell[1]] == value
    computed = board.get_empty_squares()
    computed.sort()
    expected.sort()
    assert computed == expected


@pytest.mark.parametrize(
    "cell, direction, steps, expected",
    [
        ((0, 0), DOWN, 3, [(0, 0), (1, 0), (2, 0)]),
        ((0, 1), DOWN, 3, [(0, 1), (1, 1), (2, 1)]),
        ((0, 0), DIAG_X, 3, [(0, 0), (1, 1), (2, 2)]),
        ((2, 0), RIGHT, 3, [(2, 0), (2, 1), (2, 2)]),
        ((2, 0), DIAG_Y, 3, [(2, 0), (1, 1), (0, 2)]),
    ]
)
def test_traverse_grid(cell, direction, steps, expected):
    board = TTTBoard(dim=(3, 3))
    stride = board.traverse_grid(cell, direction, steps)
    assert stride == expected


@pytest.mark.parametrize(
    "board, values",
    [
        (board_1, [
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
        ]),
        (board_4, [
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 3), (1, 3), (2, 3)],
        ]),
        (board_5, [
            [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)],
            [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)],
            [(0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
            [(0, 3), (1, 3), (2, 3), (3, 3), (4, 3)],
        ]),
    ]
)
def test_up_columns(board, values):
    board = TTTBoard(board=board)
    stride = board.up_columns()
    assert sorted(stride) == sorted(values)


@pytest.mark.parametrize(
    "board, values",
    [
        (board_1, [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
        ]),
        (board_4, [
            [(0, 0), (0, 1), (0, 2), (0, 3)],
            [(1, 0), (1, 1), (1, 2), (1, 3)],
            [(2, 0), (2, 1), (2, 2), (2, 3)],
        ]),
        (board_5, [
            [(0, 0), (0, 1), (0, 2), (0, 3)],
            [(1, 0), (1, 1), (1, 2), (1, 3)],
            [(2, 0), (2, 1), (2, 2), (2, 3)],
            [(3, 0), (3, 1), (3, 2), (3, 3)],
            [(4, 0), (4, 1), (4, 2), (4, 3)],
        ]),
    ]
)
def test_side_columns(board, values):
    board = TTTBoard(board=board)
    stride = board.side_columns()
    assert sorted(stride) == sorted(values)


@pytest.mark.parametrize(
    "dim, values",
    [
        ((3, 3), [(0, 0), (1, 1), (2, 2)]),
        ((4, 4), [(0, 0), (1, 1), (2, 2), (3, 3)]),
        ((2, 2), [(0, 0), (1, 1)]),
    ]
)
def test_diagonal_side_x(dim, values):
    board = TTTBoard(dim=dim)
    stride = board.diagonal_side_x()
    assert sorted(stride) == sorted(values)


@pytest.mark.parametrize(
    "dim, values",
    [
        ((4, 4), [(3, 0), (2, 1), (1, 2), (0, 3)]),
        ((3, 3), [(2, 0), (1, 1), (0, 2)]),
        ((2, 2), [(1, 0), (0, 1)]),
    ]
)
def test_diagonal_side_y(dim, values):
    board = TTTBoard(dim=dim)
    stride = board.diagonal_side_y()
    assert sorted(stride) == sorted(values)


@pytest.mark.parametrize(
    "board, cells, expected",
    [
        (
            board_1,
            [(0, 0), (1, 0), (2, 2)],
            [EMPTY, PLAYERX, PLAYERO],
        ),
        (
            board_4,
            [(0, 3), (1, 0), (2, 2), (2, 3), (0, 2)],
            [PLAYERX, EMPTY, PLAYERO, PLAYERX, PLAYERO],
        ),
        (
            board_5,
            [(4, 0), (1, 0), (2, 2), (1, 2), (4, 3), (3, 3)],
            [PLAYERO, EMPTY, PLAYERO, EMPTY, PLAYERX, PLAYERX],
        ),
    ]
)
def test_get_player_on_cells(board, cells, expected):
    board = TTTBoard(board=board)
    computed = board.get_player_on_cells(cells)
    assert sorted(computed) == sorted(expected)


@pytest.mark.parametrize(
    "cells, expected",
    [
        ([EMPTY, PLAYERX, PLAYERO], None),
        ([PLAYERX, EMPTY, PLAYERO, PLAYERX, PLAYERO], None),
        ([PLAYERO, EMPTY, PLAYERO, EMPTY, PLAYERX, PLAYERX], None),
        ([PLAYERO, PLAYERO, PLAYERO], PLAYERO),
        ([PLAYERX, PLAYERX, PLAYERX, PLAYERX], PLAYERX),
        ([PLAYERX, PLAYERX, PLAYERX, EMPTY], None),
    ]
)
def test_get_winner(cells, expected):
    board = TTTBoard(dim=(4, 4))
    computed = board.get_winner(cells)
    assert computed == expected


@pytest.mark.parametrize(
    "board, winner",
    [
        (board_1, None),
        (board_2, PLAYERO),
        (board_3, None),
        (board_4, None),
        (board_5, None),

        (win_board_1, PLAYERX),
        (win_board_2, PLAYERO),
        (win_board_3, PLAYERX),
        (win_board_4, PLAYERO),
        (win_board_5, DRAW),

    ]
)
def test_check_win(board, winner):
    board = TTTBoard(board=board)
    assert board.check_win() == winner


@pytest.mark.parametrize(
    "board",
    [
        board_1, board_2, board_3, board_4, board_5,
        win_board_1, win_board_2, win_board_3, win_board_4,
        win_board_5,
    ]
)
def test_clone(board):
    board = TTTBoard(board=board)
    assert board.clone() is not board._board


@pytest.mark.parametrize(
    "board",
    [
        board_1, board_2, board_3, board_4, board_5,
        win_board_1, win_board_2, win_board_3, win_board_4,
        win_board_5,
    ]
)
def test_display(board):
    board = TTTBoard(board=board)
    board.display()


@pytest.mark.parametrize(
    "player, expected",
    [
        (PLAYERX, PLAYERO),
        (PLAYERO, PLAYERX),
    ]
)
def test_switch_player(player, expected):
    computed = switch_player(player)
    assert computed == expected


@pytest.mark.parametrize(
    "board",
    [
        board_1, board_2, board_3, board_4, board_5,
        win_board_1, win_board_2, win_board_3, win_board_4,
        win_board_5,
    ]
)
def test_mc_trial(board):
    board = TTTBoard(board=board)
    copied = deepcopy(board._board)
    mc_trial(board, PLAYERX)
    if len(board.get_empty_squares()) > 0:
        assert board._board != copied
    else:
        assert len(board.get_empty_squares()) == 0


@pytest.mark.parametrize(
    "board, expected",
    [
        (board_1, score_1),
        (board_2, score_2),
        (board_5, score_5),
    ]
)
def test_mc_update_scores(board, expected: list[list[int]]):
    for player in [PLAYERO, PLAYERX]:
        board_obj = TTTBoard(board=board)
        empty_scores = [[0 for _ in row] for row in expected]
        mc_update_scores(empty_scores, board_obj, player)
        assert empty_scores == expected


@pytest.mark.parametrize(
    "dim, expected",
    [
        ((2, 2), [[0, 0], [0, 0]]),
        ((3, 3), [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        ((2, 3), [[0, 0, 0], [0, 0, 0]]),
    ]
)
def test_init_empty_scores(dim, expected):
    computed = init_empty_scores(*dim)
    assert computed == expected


@pytest.mark.parametrize(
    "board, scores, expected",
    [
        (board_1, result_1, expected_1),
        (board_2, result_2, expected_2),
        (board_5, result_5, expected_5),
    ]
)
def test_get_best_move(board, scores, expected):
    board = TTTBoard(board=board)
    computed = get_best_move(board, scores)
    assert computed == expected


def test_mc_move():
    """Test if the mc_move is returning the best move"""
    expected = (1, 2)
    values = []
    test_trials = 30
    board = TTTBoard(
        board=[[provided.PLAYERX, provided.EMPTY, provided.EMPTY], [provided.PLAYERO, provided.PLAYERO, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.EMPTY]]
    )
    for _ in range(test_trials):
        value = mc_move(board, provided.PLAYERX, NTRIALS)
        values.append(value)
    perc = (values.count(expected) / test_trials) * 100
    assert perc >= 100
