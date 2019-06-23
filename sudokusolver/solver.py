# solver.py - this is where the solving magic happens


from .common.constants import MESSAGES
from .common.board import Board


# The program starts from here
def run():
    print(MESSAGES["welcome"])

    board = Board()

    board.print_row(3)

    board.print_col(1)

    board.set_value(4, 1,1)
    print(board.get_value(4, 4))
    board.print()
