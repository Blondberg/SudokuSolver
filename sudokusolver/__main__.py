# main.py - makes it possible to run the program from terminal with
# python3 -m sudokusolver
# from sudokusolver import solver
# put solver.run() in main to run

board = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
         [6, 8, 0, 0, 7, 0, 0, 9, 0],
         [1, 9, 0, 0, 0, 4, 5, 0, 0],
         [8, 2, 0, 1, 0, 0, 0, 4, 0],
         [0, 0, 4, 6, 0, 2, 9, 0, 0],
         [0, 5, 0, 0, 0, 3, 0, 2, 8],
         [0, 0, 9, 3, 0, 0, 0, 7, 4],
         [0, 4, 0, 0, 5, 0, 0, 3, 6],
         [7, 0, 3, 0, 1, 8, 0, 0, 0]]


def solve():
    print("Trying to solve board...")
    rec_solve(0, 0)


def rec_solve(row, col):
    for i in range(1, 9):  # Loop through all possible numbers
        if is_valid(row, col, i):
            board[row][col] = i
            print_board()
            next_row, next_col = get_next_coord(row, col)
            if next_row == -1 and next_col == -1:  # we have reached the end
                return True
            if not rec_solve(next_row, next_col):
                board[row][col] = 0

    return False  # return false if no one of the numbers work


def get_next_coord(row, col):
    next_row = row + 1
    next_col = col
    if next_row == 9:
        next_row = 0
        next_col += 1
    if next_col == 9:
        return -1, -1

    return next_row, next_col


def is_valid(row, col, n):
    return not (in_square(get_square(row, col), n) or (
        in_row(row, n) or
        in_col(col, n))) and board[row][col] == 0


def get_square(row, col):
    return (row // 3) * 3 + col // 3


def in_square(square, n):
    row = square // 3
    col = square % 3
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if board[i][j] == n:
                return True
    return False


def in_row(row, n):
    return n in board[row]


def in_col(col, n):
    for row in board:
        if row[col] == n:
            return True
    return False


def print_board():
    print("####")
    for row in board:
        print(row)
    print("####")


if __name__ == '__main__':
    # Solve the sudoku
    solve()

    print_board()
