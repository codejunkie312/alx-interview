#!/usr/bin/python3
import sys
"""N queens puzzle"""


def is_safe(board, row, col, N):
    """
    Check if it is safe to place a queen at a given cell.

    Args:
        board (list): A 2D list representing the chess board.
        row (int): The row number of the cell.
        col (int): The column number of the cell.
        N (int): The size of the board.

    Returns:
        bool: True if it is safe to place a queen, otherwise False.
    """

    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """
    Utility function to solve N queens problem.

    Args:
        board (list): A 2D list representing the chess board.
        col (int): The current column number.
        N (int): The size of the board.
        solutions (list): A list to store the solutions.
    """
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j]:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = True
            solve_nqueens_util(board, col + 1, N, solutions)
            board[i][col] = False


def solve_nqueens(N):
    """
    Solve the N queens problem.

    Args:
        N (int): The size of the board.
    """

    board = [[False for j in range(N)] for i in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
