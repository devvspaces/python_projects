import sys

import pytest

sys.path.append('C:/Users/Dell/python_projects')  # noqa Edit this to fit your own directory path to the project folder
from TicTacToe.code import (SCORE_CURRENT, SCORE_OTHER, add_score,  # noqa
                            get_score_to_add)
from TicTacToe.poc_ttt_provided import PLAYERO, PLAYERX  # noqa


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
