# main.py - makes it possible to run the program from terminal with
# python3 -m sudokusolver
# from sudokusolver import solver
# put solver.run() in main to run

board = [
     [0, 0, 0, 2, 6, 0, 7, 0, 1],
     [6, 8, 0, 0, 7, 0, 0, 9, 0],
     [1, 9, 0, 0, 0, 4, 5, 0, 0],
     [8, 2, 0, 1, 0, 0, 0, 4, 0],
     [0, 0, 4, 6, 0, 2, 9, 0, 0],
     [0, 5, 0, 0, 0, 3, 0, 2, 8],
     [0, 0, 9, 3, 0, 0, 0, 7, 4],
     [0, 4, 0, 0, 5, 0, 0, 3, 6],
     [7, 0, 3, 0, 1, 8, 0, 0, 0]
    ]

solved_board = [
            [4, 3, 5, 2, 6, 9, 7, 8, 1],
            [6, 8, 2, 5, 7, 1, 4, 9, 3],
            [1, 9, 7, 8, 3, 4, 5, 6, 2],
            [8, 2, 6, 1, 9, 5, 3, 4, 7],
            [3, 7, 4, 6, 8, 2, 9, 1, 5],
            [9, 5, 1, 7, 4, 3, 6, 2, 8],
            [5, 1, 9, 3, 2, 6, 8, 7, 4],
            [2, 4, 8, 9, 5, 7, 1, 3, 6],
            [7, 6, 3, 4, 1, 8, 2, 5, 9]
        ]


def solve():
    print("Trying to solve board...")
    rec_solve(0, 0)
    print("Positions empty: ", empty_left())


def rec_solve(row, col):
    next_row, next_col = get_next_coord(row, col)

    print("Rec solve is called")
    print("Looking at row: ", row, ", col: ", col)
    if board[row][col] == 0:
        for i in range(1, 10):  # Loop through all possible numbers
            print("Testing value: ", i)
            if board[row][col] == 0:
                if is_valid(row, col, i):
                    board[row][col] = i
                    print_board(board)
                    if next_row == -1 and next_col == -1:  # board completed
                        return True
                    if not rec_solve(next_row, next_col):
                        board[row][col] = 0
                    else:
                        return True
                else:
                    board[row][col] = 0
    else:
        return rec_solve(next_row, next_col)


# Get the next pposition to look at
def get_next_coord(row, col):
    next_row = row
    next_col = col + 1
    if next_col == 9:
        next_col = 0
        next_row += 1
    if next_row == 9:
        return -1, -1

    return next_row, next_col


# Check if the value n is valid on picked position
def is_valid(row, col, n):
    return not (in_square(get_square(row, col), n) or (
        in_row(row, n) or
        in_col(col, n)))


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


# Print out the game board in its current state
def print_board(board):
    print("####")
    for row in board:
        print(row)
    print("####")


# Check amount of empty positions left on the board
def empty_left():
    empty_positions = 0

    for row in board:
        for n in row:
            if n == 0:
                empty_positions = empty_positions + 1

    return empty_positions


if __name__ == '__main__':
    # Solve the sudoku
    solve()

    print("\n Solution")
    print_board(board)
    print("\n Correct solution")
    print_board(solved_board)
