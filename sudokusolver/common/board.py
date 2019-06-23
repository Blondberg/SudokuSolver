# board.py - contains the sudoku board and print functions for it

from .test_boards import EASY1


class Board(object):

    # Set local fields
    def __init__(self):
        print("Board created")
        self.board = EASY1['unsolved']
        self.board_size = 9

    # Print the board in a pleasant way
    def print(self):
        print("Printing the board for your viewing pleasures")

        print(' ' + '=' * 29)

        for row in range(self.board_size):
            print("|", end='')
            for col in range(self.board_size):
                print(" " + str(self.board[row][col]).replace('0', '□') + " ", end='')

                if (col + 1) % 3 == 0:
                    print("|", end='')

            print()
            if (row + 1) % 3 == 0:
                print(' ' + '=' * 29)

    # Print the board in an un-pleasant way, for debugging purposes etc.
    def print_raw(self):
        print("Printing an ugly board for the array nerds out there")
        for row in range(self.board_size):
            print(self.board[row])

    # Print row of choice, not a good looking output
    def print_row(self, n):
        print(str(self.board[n - 1]).replace('0', '□ '))

    # Print col of choice, not a good looking output
    def print_col(self, n):
        for row in range(self.board_size):
            print(str(self.board[row][n - 1]).replace('0', '□'))

    # Get value from chosen position
    def get_value(self, col, row):
        return self.board[row - 1][col - 1]

    # Set value of chosen position
    def set_value(self, n, col, row):
        self.board[row - 1][col - 1] = n
