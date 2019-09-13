# main.py - makes it possible to run the program from terminal with
# python3 -m sudokusolver

from .common.board import Board

from sudokusolver.solver import solve

import sudokusolver.common.messenger as msgr

# The program starts from here
def run():
    msgr.info("Welcome to the python Sudoku Solver!")

    board = Board()

    board.print()

    solve(board)


if __name__ == '__main__':
    run()
