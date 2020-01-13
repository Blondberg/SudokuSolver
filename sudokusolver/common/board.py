# board.py - contains the sudoku board and print functions for it

import SudokuSolver.sudokusolver.common.messenger as msgr
from .test_boards import TOP_ROW1


class Board(object):

    # Set local fields
    def __init__(self):
        msgr.action("Board created")
        self.board = TOP_ROW1['unsolved']
        self.size = 9

    # Print the board in a pleasant way
    def print(self):
        msgr.action("Printing the board for your viewing pleasures")

        print(' ' + '=' * 29)

        for row in range(self.size):
            print("|", end='')
            for col in range(self.size):
                print(" " + str(self.board[row][col]).replace('0', '□') + " ", end='')

                if (col + 1) % 3 == 0:
                    print("|", end='')

            print()
            if (row + 1) % 3 == 0:
                print(' ' + '=' * 29)

    # Print the board in an un-pleasant way, for debugging purposes etc.
    def print_raw(self):
        print("Printing an ugly board for the array nerds out there")
        for row in range(self.size):
            print(self.board[row])

    # Print row of choice, not a good looking output
    def print_row(self, n):
        print(str(self.board[n - 1]).replace('0', '□ '))

    # Print col of choice, not a good looking output
    def print_col(self, n):
        for row in range(self.size):
            print(str(self.board[row][n - 1]).replace('0', '□'))

    # Get value from chosen position
    def get_value(self, col, row):
        return self.board[row - 1][col - 1]

    # Set value of chosen position
    # Takes in the value and a tuple for the coordinate
    def set_value(self, coord, n):
        if isinstance(coord, tuple):
            self.board[tuple(coord)[1] - 1][tuple(coord)[0] - 1] = n
        else:
            msgr.error("The coordinate needs to be a tuple, (col, row)!")

    # Check if value v exists in row
    def value_in_row(self, row, v):
        return v in self.board[row - 1]

    # Check if value v exists in col
    def value_in_col(self, col, v):
        for row in self.board:
            if v == row[col - 1]:
                return True
        return False

    """def value_in_square(self, sqr_n, v):
        for row in range()
    """
