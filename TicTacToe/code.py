"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
from typing import List, Tuple, Type

from . import poc_ttt_provided as provided

# import poc_ttt_gui
# import poc_ttt_provided as provided


# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1          # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0    # Score for squares played by the other player

# Add your functions here.


def mc_trial(board: Type[provided.TTTBoard], player):
    """
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player by
    making random moves, alternating between players.
    The modified board will contain the state of the game,

    :param board: current board for trial
    :type board: Type[provided.TTTBoard]
    :param player: Player to move next
    :type player: int
    """
    empty_list: list = board.get_empty_squares()
    count_empty_list = len(empty_list)
    current_player = player
    for _ in range(count_empty_list):
        position = random.choice(empty_list)
        board.move(*position, current_player)
        current_player = provided.switch_player(current_player)
        empty_list.remove(position)


def add_score(player, value):
    if player != value:
        return SCORE_CURRENT
    return SCORE_OTHER


def get_score_to_add(player, winner, value):
    if value == winner:
        return add_score(player, value)
    else:
        return -add_score(player, value)


def mc_update_scores(
    scores: List[List[int]], board: Type[provided.TTTBoard], player: int
):
    winner = board.check_win()
    if winner == provided.DRAW:
        return
    board_dim = board.get_dim()
    for row in range(board_dim[0]):
        for col in range(board_dim[1]):
            value = board.square(row, col)
            scores[row][col] += get_score_to_add(player, winner, value)


def get_best_move(board: Type[provided.TTTBoard], scores) -> Tuple[int]:
    empty_positions = board.get_empty_squares()
    best_score = None
    max_score = 0
    for row, col in empty_positions:
        score = scores[row][col]
        if score > max_score:
            max_score = score
            best_score = (row, col)
    return best_score


def mc_move(board, player, trials):
    pass





# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
