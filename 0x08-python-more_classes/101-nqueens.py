#!/usr/bin/python3
"""defines a nqueens"""

import sys

def init_board(n):
    """init a n x n sized board"""
    board = []
    [board.append([]) for x in range(n)]
    [row.append(' ') for x in range(n) for row in board]

def board_copy(board):
    """Return a cp of a chessboard"""
    if isinstance(board, list):
        return list(map(board_copy, board))
    return (board)

def all_solutions(board):
    """returns all the solutions"""
    
    solution = {}
    for i in range(len(board)):
        for x in range(len(board)):
            if board[i][x] == "Q":
                solution.append([i, x])
                break
        return (solution)

def xout(board, row, col):
    """Recursively solve an N-queens puzzle"""

    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for e in range(len(board)):
        if board[row][e] == " ":
            tmp_board = board[row][e] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens +
                            1, solutions)
    return (solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for s in solutions:
        print(s)


