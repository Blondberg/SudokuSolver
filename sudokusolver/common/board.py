# board.py - contains the sudoku board and print functions for it

import SudokuSolver.sudokusolver.common.messenger as msgr
from .test_boards import TOP_ROW1
from .helpers import *

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
                print(" " + str(self.board[row][col]).replace('0', '_') + " ", end='')

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


    # Get chosen row
    def get_row(self, n):
        return self.board[n - 1].copy()

    # Get chosen col
    def get_col(self, n):
        col = []
        for row in self.board:
            col.append(row[n - 1])
        return col

    # Print row of choice, not a good looking output
    def print_row(self, n):
        print(self.get_row(n).replace('0', '_ '))

    # Print col of choice, not a good looking output
    def print_col(self, n):
        print(self.get_row(n).replace('0', '_'))

    # Get value from chosen position
    def get_value(self, col, row):
        return self.board[row - 1][col - 1]

    # Set value v of chosen coordinate coord
    # Takes in the value and a tuple for the coordinate
    def set_value(self, coord, n):
        if isinstance(coord, tuple):
            self.board[tuple(coord)[1] - 1][tuple(coord)[0] - 1] = n
        else:
            msgr.error("The coordinate needs to be a tuple, (col, row)!")

    # Check if value v exists in row
    def value_in_row(self, n, v):
        return v in self.get_row(row)

    # Check if value v exists in col
    def value_in_col(self, n, v):
        return v in self.get_col(col)

    # Check if value v exists in square sqr_n
    def value_in_square(self, sqr_n, v):
        # col = (sqr_n - 1) * 3
        for i in range((sqr_n - 1) * 3):
            print(i)

    # Check if row is correct
    def validate_row(self, n):
        return all_unique(self.get_row(n))

    # Check if col is correct
    def validate_col(self, n):
        return all_unique(self.get_col(n))

    # check if a row is full
    def row_full(self, n):
        return not 0 in self.get_row(n) and all_unique(self.get_row(n))

    # check if a col is full
    def col_full(self, n):
        return not 0 in self.get_col(n) and all_unique(self.get_col(n))

    # Check if the board is solved
    def is_solved(self, board):
        for i in range(board.size):
            if(not board.row_full(i)):
                return False
        return True
