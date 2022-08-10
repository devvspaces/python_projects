"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
from typing import List, Tuple, Type

import sys
sys.path.append('C:/Users/Dell/python_projects')  # noqa
from TicTacToe import poc_ttt_provided as provided

# import poc_ttt_gui
# import poc_ttt_provided as provided


# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 100        # Number of trials to run
SCORE_CURRENT = 1.0  # Score for squares played by the current player
SCORE_OTHER = 1.0    # Score for squares played by the other player

# Add your functions here.


T = Type[provided.TTTBoard]


def mc_trial(board: T, player):
    """
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player by
    making random moves, alternating between players.
    The modified board will contain the state of the game,

    :param board: current board for trial
    :type board: T
    :param player: Player to move next
    :type player: int
    """
    empty_list: list = board.get_empty_squares()
    count_empty_list = len(empty_list)
    current_player = player
    for _ in range(count_empty_list):
        position = random.choice(empty_list)
        board.move(*position, current_player)
        if board.check_win() == current_player:
            break
        current_player = provided.switch_player(current_player)
        empty_list.remove(position)


def add_score(player, value):
    """Get the score to add depending on the current player
    and the winner"""
    if player != value:
        return SCORE_CURRENT
    return SCORE_OTHER


def get_score_to_add(player, winner, value):
    """Get the score to add to the board cell"""
    if value == winner:
        return add_score(player, value)
    else:
        return -add_score(player, value)


def mc_update_scores(
    scores: List[List[int]], board: T, player: int
):
    """
    This function takes a grid of scores (a list of lists)
    with the same dimensions as the Tic-Tac-Toe board, a
    board from a completed game, and which player the machine
    player is. The function should score the completed board
    and update the scores grid. As the function updates
    the scores grid directly, it does not return anything,

    :param scores: _description_
    :type scores: List[List[int]]
    :param board: _description_
    :type board: T
    :param player: the machine player
    :type player: int
    """
    winner = board.check_win()
    if winner is None or winner == provided.DRAW:
        return
    board_dim = board.get_dim()
    for row in range(board_dim[0]):
        for col in range(board_dim[1]):
            value = board.square(row, col)
            scores[row][col] += get_score_to_add(player, winner, value)


def get_best_move(board: T, scores) -> Tuple[int]:
    """
    This function takes a current board and a grid of
    scores. The function should find all of the empty
    squares with the maximum score and randomly return
    one of them as a (row, column) tuple.
    It is an error to call this function with a
    board that has no empty squares (there is no
    possible next move), so your function may do
    whatever it wants in that case. The case where
    the board is full will not be tested.
    """
    empty_positions = board.get_empty_squares()
    best_score = empty_positions[0]
    max_score = 0
    for row, col in empty_positions:
        score = scores[row][col]
        if score >= max_score:
            max_score = score
            best_score = (row, col)
    return best_score


def init_empty_scores(row, col):
    """
    Takes in a row x col dimension and returns
    empty scores
    """
    scores = []
    for _ in range(row):
        rows = []
        for _ in range(col):
            rows.append(0)
        scores.append(rows)

    return scores


def mc_move(board: T, player, trials):
    """
    This function takes a current board, which player the machine
    player is, and the number of trials to run. The function should
    use the Monte Carlo simulation described above to return a move
    for the machine player in the form of a (row, column) tuple.
    Be sure to use the other functions you have written!
    """

    scores = init_empty_scores(*board.get_dim())

    # count = 0

    for _ in range(trials):
        # Clone current board
        clone = board.clone()

        # print("before")
        # print(clone.display(), '\n\n')

        # Run a trial simulation
        mc_trial(clone, player)

        # print("after")
        # print(clone.display(), '\n\n')

        # Score board cloned, Updates Scores
        mc_update_scores(scores, clone, player)
        # clone.display()
        # if clone.check_win() == provided.PLAYERO:
        #     count += 1

    # print("machine player won", count, "times")

    # Get Best move
    best_move = get_best_move(board, scores)
    # print(scores)
    return best_move


# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
