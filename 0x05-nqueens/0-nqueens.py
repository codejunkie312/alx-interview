#!/usr/bin/python3
"""N queens puzzle"""
import sys


def is_safe(board, row, col, n):
    """Check if a queen can be placed on board[row][col]"""
    for c in range(col):
        if board[c] == row or \
           board[c] - c == row - col or \
           board[c] + c == row + col:
            return False
    return True


def solve(board, col, n):
    """Solve the N queens puzzle"""
    if col == n:
        print(str([[c, board[c]] for c in range(n)]))
        return
    for row in range(n):
        if is_safe(board, row, col, n):
            board[col] = row
            solve(board, col + 1, n)


if __name__ == "__main__":
    solve([0 for i in range(int(sys.argv[1]))], 0, int(sys.argv[1]))
