# main.py - makes it possible to run the program from terminal with
# python3 -m sudokusolver
# from sudokusolver import solver
# put solver.run() in main to run


def solve(board):
    rec_solve(board, 0, 0)

def rec_solve(board, row, col):
    for i in range(0, 9):
        if is_valid(board, row, col, n):
            


def is_valid(board, row, col, n):
    return in_square(board, get_square(board, row, col), n) or
    in_row(board, row, n) or
    in_col(board, col, n)


def get_square(board, row, col):
    return (row // 3) * 3 + col // 3


def in_square(board, square, n):
    row = square // 3
    col = square % 3
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if board[i][j] == n:
                return True
    return False


def in_row(board, row, n):
    return n in board[row]


def in_col(board, col, n):
    for row in board:
        if row[col] == n:
            return True
    return False


if __name__ == '__main__':
    # Solve the sudoku
    solve([[0, 0, 0, 2, 6, 0, 7, 0, 1],
           [6, 8, 0, 0, 7, 0, 0, 9, 0],
           [1, 9, 0, 0, 0, 4, 5, 0, 0],
           [8, 2, 0, 1, 0, 0, 0, 4, 0],
           [0, 0, 4, 6, 0, 2, 9, 0, 0],
           [0, 5, 0, 0, 0, 3, 0, 2, 8],
           [0, 0, 9, 3, 0, 0, 0, 7, 4],
           [0, 4, 0, 0, 5, 0, 0, 3, 6],
           [7, 0, 3, 0, 1, 8, 0, 0, 0]])
