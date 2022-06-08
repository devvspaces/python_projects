"""
Clone of 2048 game.
To play this game online, head to https://py3.codeskulptor.org/#user307_biorjpH9nC_15.py and click on run
"""

# import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    result = [line[0]]

    for item in line[1:]:
        if item != 0:
            if result[-1] == item:
                result[-1] += item
                result.append(0)
            else:
                if result[-1] == 0:
                    result[-1] = item
                else:
                    result.append(item)
        
    
    return result + [0 for _ in range(len(line) - len(result))]


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code

        self._grid_width = grid_width
        self._grid_height = grid_height

        self._initials = {

            UP: self.traverse_grid(
                (0,0,), (0, 1,), self.get_grid_width()
            ),

            DOWN: self.traverse_grid(
                (self.get_grid_height() - 1, 0,),
                (0, 1,), self.get_grid_width()
            ),

            LEFT: self.traverse_grid(
                (0, 0,),
                (1, 0,), self.get_grid_height()
            ),

            RIGHT: self.traverse_grid(
                (0, self.get_grid_width() - 1,),
                (1, 0,), self.get_grid_height()
            ),

        }

        self._steps = {
            UP: self.get_grid_height(),
            DOWN: self.get_grid_height(),
            LEFT: self.get_grid_width(),
            RIGHT: self.get_grid_width(),
        }

        self._board = []
        self._cell_board = []
        self._failed = False

        self.reset()

    def traverse_grid(self, start_cell, direction, num_steps):
        """
        Function that iterates through the cells in a grid
        in a linear direction
        
        Both start_cell is a tuple(row, col) denoting the
        starting cell
        
        direction is a tuple that contains difference between
        consecutive cells in the traversal
        """

        stride = []
        
        for step in range(num_steps):
            row = start_cell[0] + step * direction[0]
            col = start_cell[1] + step * direction[1]
            stride.append((row, col,))
        
        return stride

    def create_empty_grid(self, row, col):
        """
        Creates and empty grid on row by col filled with zeros
        """
        return [[0 for _ in range(col)] for _ in range(row)]
    
    def count_empty_cells(self):
        """
        Return the amount of empty cells
        """
        return len(self._cell_board)
    
    def remove_from_cell(self, row, col):
        """
        Removes an index from the cell board
        """
        index = (row, col,)
        try:
            self._cell_board.remove(index)
        except ValueError:
            pass
    
    def add_cell(self, row, col):
        """
        Adds an index from the cell board
        """
        index = (row, col,)
        if index not in self._cell_board:
            self._cell_board.append(index)

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        
        grid_height = self.get_grid_height()
        grid_width = self.get_grid_width()

        new_grid = self.create_empty_grid(grid_height, grid_width)
        self._board = new_grid

        for row in range(grid_height):
            for col in range(grid_width):
                self.add_cell(row, col)

        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        result = ''
        result += '-' * len(self.get_grid()[0]) * 4 + '\n'
        for row in self.get_grid():
            for col in row:
                result += "| {} ".format(col)

            result += '|\n'
            result += '-' * len(row) * 4 + '\n'

        return result

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width
    
    def get_grid(self):
        """
        Returns the game grid
        """
        return self._board
    
    def get_direction_command(self, direction):
        """
        Get a direction command
        """
        return OFFSETS[direction]
    
    def get_direction_step(self, direction):
        """
        Get a direction number of step to move
        """
        return self._steps[direction]

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        
        # Get initials
        initials = self._initials[direction]

        m_direction = self.get_direction_command(direction)
        m_steps = self.get_direction_step(direction)

        updated = False

        for init in initials:
            trav_indexes = self.traverse_grid(init, m_direction, m_steps)
            trav_values = [self.get_tile(index[0], index[1]) for index in trav_indexes]
            merged_values = merge(trav_values)
            for old, new, index in zip(trav_values, merged_values, trav_indexes):
                if old != new:
                    self.set_tile(index[0], index[1], new)
                    updated = True
        
        if updated:
            self.new_tile()
            

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """

        if self.count_empty_cells() > 0:
            
            index = random.choice(self._cell_board)
            
            value = random.randint(1, 10)
            value = 2 if value < 10 else 4

            #print(f'New tile position: Row {index[0]} x Col {index[1]}')

            self.set_tile(index[0], index[1], value)
        
        else:
            self._failed = True
            print('No empty cells')

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._board[row][col] = value
        if value != 0:
            self.remove_from_cell(row, col)
        else:
            self.add_cell(row, col)

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.get_grid()[row][col]

    def is_game_won(self):
        """
        Checks if game is won
        """
        if self._failed != True:
            for row in self.get_grid():
                for col in row:
                    if col == 2048:
                        return True
        return False
    
    def play(self):
        """
        Play game with inputs
        """

        while self.is_game_won() == False:
            print('Current Board')
            print(self)

            direction = input('Where do you want to move? UP(1) DOWN(2) LEFT(3) RIGHT(4): ')
            if direction not in list('1234'):
                print('Please enter a valid option')
                continue
            
            self.move(int(direction))



# poc_2048_gui.run_gui(TwentyFortyEight(4, 4))


"""
Test suite for TwentyFortyEight

Using my custom simple test suite package for python 
"""
import sys

sys.path.append('C:/Users/Dell/python_projects') # Edit this to fit your own directory path to the project folder

from Simple_test_suite.suite import MyTestSuite


def run_suite():
    """
    Some testing code
    """
    
    # create a TestSuite object
    suite = MyTestSuite()

    # Testing merge function
    suite.run_test(merge([2,0,2,2]), [4,2,0,0])
    suite.run_test(merge([2,2,2,2]), [4,4,0,0])
    suite.run_test(merge([2,8,8,2]), [2,16,2,0])


    # Test game

    game = TwentyFortyEight(4, 5)

    for _ in range(4):
        game.new_tile()

    suite.run_test(game.count_empty_cells(), 14)
    suite.run_test(game.get_grid_height(), 4)
    suite.run_test(game.get_grid_width(), 5)

    index = game._cell_board[0]
    game.set_tile(*index, 4)
    suite.run_test(game.get_tile(*index), 4)


    # More tests
    obj = TwentyFortyEight(4, 4)
    obj.set_tile(0, 0, 2)
    obj.set_tile(0, 1, 4)
    obj.set_tile(0, 2, 8)
    obj.set_tile(0, 3, 16)
    obj.set_tile(1, 0, 16)
    obj.set_tile(1, 1, 8)
    obj.set_tile(1, 2, 4)
    obj.set_tile(1, 3, 2)
    obj.set_tile(2, 0, 0)
    obj.set_tile(2, 1, 0)
    obj.set_tile(2, 2, 8)
    obj.set_tile(2, 3, 16)
    obj.set_tile(3, 0, 0)
    obj.set_tile(3, 1, 0)
    obj.set_tile(3, 2, 4)
    obj.set_tile(3, 3, 2)
    obj.move(UP)

    suite.run_test(obj.count_empty_cells(), 4)
    suite.run_test(obj.get_grid(), [[2, 4, 8, 16], [16, 8, 4, 2], [0, 0, 8, 16], [0, 0, 4, 2]])
    
    
    suite.fetch_results()


# Command to run tests
# run_suite()