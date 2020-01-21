# main.py - makes it possible to run the program from terminal with
# python3 -m sudokusolver
# from sudokusolver import solver
# put solver.run() in main to run


# Run to solve the board
def solve():
    rec_solve(0, 0)


# Recusive function that solves the board
def rec_solve(row, col):
    next_row, next_col = get_next_coord(row, col)

    if board[row][col] == 0:
        for i in range(1, 10):  # Loop through all possible numbers
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


# Get square number based on row and col
def get_square(row, col):
    return (row // 3) * 3 + col // 3


# Check if value exists in square
def in_square(square, n):
    row = square // 3 * 3
    col = square % 3 * 3
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if board[i][j] == n:
                return True
    return False


# Check if value exists in row
def in_row(row, n):
    return n in board[row]


# Check if value exists in col
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


board_1 = [
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

board_2 = [
     [0, 0, 0, 2, 6, 0, 0, 0, 1],
     [0, 0, 0, 0, 7, 0, 0, 0, 0],
     [0, 9, 0, 0, 0, 4, 5, 0, 0],
     [0, 2, 0, 1, 0, 0, 0, 4, 0],
     [0, 0, 4, 0, 0, 2, 0, 0, 0],
     [0, 0, 0, 0, 0, 3, 0, 2, 8],
     [0, 0, 0, 3, 0, 0, 0, 0, 4],
     [0, 4, 0, 0, 0, 0, 0, 3, 0],
     [7, 0, 3, 0, 1, 0, 0, 0, 0]
    ]

if __name__ == '__main__':
    # Solve the sudoku
    board = board_1
    solve()

    print("\n Solution")
    print_board(board)
