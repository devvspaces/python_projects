# Python Clone for GAME 2048
> Amazing  Tic Tac Toe project, which makes use of [Monte Carlo Method](https://en.wikipedia.org/wiki/Monte_Carlo_method) to help the computer play smartly against you. The python script uses a Monte carlo simulation to play the game a lot of time and chooses the best move for the computer (Machine player). To play this game online, head to [CodeSkulptor](https://py2.codeskulptor.org/#user49_kMwFzdsyZ0_8.py) and run code. Also, you can also play game on your terminal by running the script.


## Requirements  (Prerequisites)
Tools and packages required to successfully install this project.
* Python 3.3 and up


## Installation

```bash
git clone https://github.com/devvspaces/python_projects`
cd python_projects
cd TicTacToe
pip install -r requirements.txt
pytest
```

Uncomment the line in code.py containing (Line 179)
```python
provided.play_game(mc_move, NTRIALS, False)
```
Then run `python code.py` in the cmd


## Features
* Can play on any type of Square grid 2 x 2, 4 x 4, 11 x 11 on [CodeSkulptor](https://py2.codeskulptor.org/#user49_kMwFzdsyZ0_8.py)
* Can play on any type of Square or Rectangular Grid locally on the cli
* Full 100% test coverage using pytest, added an important test to make sure that the computer always makes the best choices.
* You can tweak the monte carlo simulation trials to make the computer more smarter


## Running the tests

To run tests on the code;

1. Go to the TicTacToe project directory

2. Make sure the line playing the game on the cli is commented out in code.py file
```python
provided.play_game(mc_move, NTRIALS, False)
```
3. Run `pytest` in the 



## Tech Stack / Built With
1. Python only
2. Pytest for running tests
3. Coverage for test coverage
