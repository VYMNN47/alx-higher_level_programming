#!/usr/bin/python3
"""defines a nqueens"""

import sys

def init_board(n):
    """init a n x n sized board"""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board

def board_copy(board):
    """Return a cp of a chessboard"""
    if isinstance(board, list):
        return list(map(board_copy, board))
    return (board)

def all_solutions(board):
    """returns all the solutions"""
    
    solutions = []
    for i in range(len(board)):
        for x in range(len(board)):
            if board[i][x] == "Q":
                solution.append([i, x])
                break
        return (solutions)

def xout(board, row, col, queens, solutions):
    """Recursively solve an N-queens puzzle"""

    if queens == len(board):
        solutions.append(all_solutions(board))
        return (solutions)

    for e in range(len(board)):
        if board[row][e] == " ":
            tmp_board = board_copy(board)
            tmp_board[row][e] = "Q"
            solutions = xout(tmp_board, row + 1, col, queens + 1, solutions)
    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    board = init_board(n)
    solutions = xout(board, 0, 0, 0, [])

    for s in solutions:
        print(s)

