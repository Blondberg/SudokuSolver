# solver.py - this is where the solving magic happens
import sudokusolver.common.messenger as msgr
from .common.board import Board


# The program starts from here
def run():
    msgr.info("Welcome to the python Sudoku Solver!")

    board = Board()

    board.set_value((1, 1), 4)

    board.print()

    board.value_in_square(1, 4)
    # solve_board(board_object.board)


# Try to solve the chosen board
def solve_board(board):
    check_rows(board)


# Takes in a board and checks if any row can be completed
def check_rows(board):
    # Check each row if only one value is missing
    msgr.action("Checking rows...")

    """for row in board:
        if len([j for j, x in enumerate(row) if x == 0]) == 1:

"""
