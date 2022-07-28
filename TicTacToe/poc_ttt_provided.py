import copy
from typing import List, Tuple


EMPTY = 0
PLAYERX = 1
PLAYERO = 2
DRAW = 3


class TTTBoard:
    """
    Class to represent a Tic-Tac-Toe board.
    """

    def __init__(
        self, dim: Tuple[int], reverse=False, board: List[List[int]] = None
    ):
        """
        Initialize the TTTBoard object with the given dimension and
        whether or not the game should be reversed.
        """
        self._dim = dim
        self._board = board
        if self._board is None:
            self.setup_board()
        self._empty_squares: List[Tuple[int, int]] = []
        self.set_empty_squares()

    def setup_board(self):
        """
        Takes i(row) and j(col) and set a board of size i x j
        """
        board = []
        row, col = self.get_dim()
        for _ in range(row):
            row_positions = []
            for _ in range(col):
                row_positions.append(0)
            board.append(row_positions)
        self._board = board

    def __str__(self):
        """
        Human readable representation of the board.
        """
        for row in self._board:
            print(row)

    def get_dim(self) -> Tuple[int, int]:
        """
        Return the dimension of the board.
        """
        return self._dim

    def get_height(self) -> int:
        """
        Return the row dim as the height
        """
        return self.get_dim()[0]

    def get_width(self) -> int:
        """
        Return the col dim as the width
        """
        return self.get_dim()[1]

    def square(self, row: int, col: int):
        """
        Returns one of the three constants EMPTY, PLAYERX, or PLAYERO
        that correspond to the contents of the board at position (row, col).
        """
        return self._board[row][col]

    def set_empty_squares(self):
        """
        Set the _empty_squares to the cells with zero value
        in the board
        """
        empty = []
        row, col = self.get_dim()
        for _row in range(row):
            for _col in range(col):
                value = self.square(_row, _col)
                if value == 0:
                    empty.append((_row, _col))
        self._empty_squares = empty

    def get_empty_squares(self) -> list:
        """
        Return a list of (row, col) tuples for all empty squares
        """
        return copy.deepcopy(self._empty_squares)

    def remove_empty_square(self, row: int, col: int):
        """
        Remove a tuple of (row, col) from the list of empty squares
        """
        return self._empty_squares.remove((row, col))

    def move(self, row: int, col: int, player: int):
        """
        Place player on the board at position (row, col).
        player should be either the constant PLAYERX or PLAYERO.
        Does nothing if board square is not empty.
        """
        value = self.square(row, col)
        if value != 0:
            self._board[row][col] = player
            self.remove_empty_square(row, col)

    def traverse_grid(self, start_cell, direction, num_steps):
        """
        Function that iterates through the cells in a grid
        in a linear direction.
        Both start_cell is a tuple(row, col) denoting the
        starting cell.
        direction is a tuple that contains difference between
        consecutive cells in the traversal.
        """
        stride = []
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            stride.append((row, col,))
        return stride

    def up_columns(self):
        ups = self.traverse_grid(
            (0, 0),
            (0, 1),
            self.get_width()
        )
        all_ups = []
        for top in ups:
            _up = self.traverse_grid(
                top,
                (1, 0),
                self.get_height()
            )
            all_ups.append(_up)
        return all_ups

    def side_columns(self):
        sides = self.traverse_grid(
            (0, 0),
            (1, 0),
            self.get_height()
        )
        all_sides = []
        for side in sides:
            _side = self.traverse_grid(
                side,
                (0, 1),
                self.get_width()
            )
            all_sides.append(_side)
        return all_sides

    def diagonal_side_x(self):
        pass

    def check_win(self) -> int:
        """
        Returns a constant associated with the state of the game
            If PLAYERX wins, returns PLAYERX.
            If PLAYERO wins, returns PLAYERO.
            If game is drawn, returns DRAW.
            If game is in progress, returns None.
        """

    def clone(self):
        """
        Return a copy of the board.
        """
        return copy.deepcopy(self)


def switch_player(player: int):
    """
    Switches players

    :param player: int
    :type player: int
    """
    if player == PLAYERX:
        return PLAYERO
    return PLAYERX


def play_game(mc_move, trials, reverse):
    pass
