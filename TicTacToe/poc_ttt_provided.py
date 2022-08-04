import copy
from typing import List, Tuple

from .constants import (DIAG_X, DIAG_Y, DOWN, DRAW, EMPTY, RIGHT, PLAYERO,
                        PLAYERX)


def get_board_dim(board: List[list]):
    return (len(board), len(board[0]))


class TTTBoard:
    """
    Class to represent a Tic-Tac-Toe board.
    """

    def __init__(
        self, dim: Tuple[int] = None,
        reverse=False, board: List[List[int]] = None
    ):
        """
        Initialize the TTTBoard object with the given dimension and
        whether or not the game should be reversed.
        """

        if board is None:
            self._dim = dim
            self.setup_board()
        else:
            self._board = copy.deepcopy(board)
            self._dim = get_board_dim(board)

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
                row_positions.append(EMPTY)
            board.append(row_positions)
        self._board = board

    def __str__(self):
        """
        Human readable representation of the board.
        """
        for row in self._board:
            print(row)

    def display(self):
        self.__str__()

    def get_dim(self) -> Tuple[int, int]:
        """
        Return the dimension of the board.
        """
        return self._dim

    def is_square(self):
        """Checks if the board has equal sides"""
        return self.get_width() == self.get_height()

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
                if value == EMPTY:
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
        if value == EMPTY:
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
        """
        Returns all vertical columns in the board
        """
        ups = self.traverse_grid(
            (0, 0),
            RIGHT,
            self.get_width()
        )
        all_ups = []
        for top in ups:
            _up = self.traverse_grid(
                top,
                DOWN,
                self.get_height()
            )
            all_ups.append(_up)
        return all_ups

    def side_columns(self):
        """
        Returns all horizontal columns in the board
        """
        sides = self.traverse_grid(
            (0, 0),
            DOWN,
            self.get_height()
        )
        all_sides = []
        for side in sides:
            _side = self.traverse_grid(
                side,
                RIGHT,
                self.get_width()
            )
            all_sides.append(_side)
        return all_sides

    def diagonal_side_x(self):
        """
        Returns all top-left to bottom-right cells in the board
        ```
        |x|-|-|
        |-|x|-|
        |-|-|x|
        ```
        """
        side = self.traverse_grid(
            (0, 0),
            DIAG_X,
            self.get_height()
        )
        return side

    def diagonal_side_y(self):
        """
        Returns all bottom-left to top-right cells in the board
        ```
        |-|-|x|
        |-|x|-|
        |x|-|-|
        ```
        """
        side = self.traverse_grid(
            (self.get_height() - 1, 0),
            DIAG_Y,
            self.get_height()
        )
        return side

    def get_player_on_cells(self, list_of_cells):
        """
        Maps row,col values to actual cell values on board
        """
        return [
            self.square(row, col)
            for row, col in list_of_cells
        ]

    def get_winner(self, players_cells: list):
        """
        Takes a list of players and returns the
        unique player if available or None
        """
        if players_cells.count(PLAYERX) == len(players_cells):
            return PLAYERX
        if players_cells.count(PLAYERO) == len(players_cells):
            return PLAYERO

    def check_win(self) -> int:
        """
        Returns a constant associated with the state of the game
            If PLAYERX wins, returns PLAYERX.
            If PLAYERO wins, returns PLAYERO.
            If game is drawn, returns DRAW.
            If game is in progress, returns None.
        """

        for cells in self.up_columns():
            cell_values = self.get_player_on_cells(cells)
            winner = self.get_winner(cell_values)
            if winner is not None:
                return winner

        for cells in self.side_columns():
            cell_values = self.get_player_on_cells(cells)
            winner = self.get_winner(cell_values)
            if winner is not None:
                return winner

        if self.is_square():
            # Check for diagonals
            cell_values = self.get_player_on_cells(self.diagonal_side_x())
            winner = self.get_winner(cell_values)
            if winner is not None:
                return winner

            cell_values = self.get_player_on_cells(self.diagonal_side_y())
            winner = self.get_winner(cell_values)
            if winner is not None:
                return winner

        if len(self.get_empty_squares()) == 0:
            return DRAW

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
