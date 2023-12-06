#!/usr/bin/python3
"""
Solution to the nqueens problem
"""

import sys

def is_safe(board, row, col, n):
    # Check if there is a queen in the same row on the left
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check if there is a queen in the upper diagonal on the left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the lower diagonal on the left
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens_util(board, col, n):
    if col == n:
        # Found a solution, print it
        for i in range(n):
            print("[{}, {}]".format(i, board[i][col - 1]), end=" ")
        print()
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            # Place queen and move to the next column
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, n)
            # Backtrack: remove the queen to explore other possibilities
            board[i][col] = 0

def solve_nqueens(n):
    # Check if N is an integer greater or equal to 4
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the chessboard
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Start solving the N queens problem
    solve_nqueens_util(board, 0, n)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: {} N".format(sys.argv[0]))
        sys.exit(1)

    # Extract N from command line arguments
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
