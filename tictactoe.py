"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_amount = 0
    o_amount = 0
    for i in board:
        for j in i:
            if j == X:
                x_amount += 1
            if j == O:
                o_amount += 1
    if x_amount > o_amount:
        return O
    elif o_amount == x_amount:
        return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                result_set.add((i,j))

    return result_set
                
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_deep_copy = copy.deepcopy(board)
    i = action[0]
    j = action[1]
    board_deep_copy[i][j] = player(board)
    return board_deep_copy
    raise RuntimeError from exc


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    options = [X,O]
    for player in options:
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return player
        elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return player
        i = 0
        for j in range(3):
            if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player:
                return player
            elif board[j][i] == player and board[j][i+1] == player and board[j][i+2] == player:
                return player
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == None:
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    return False
                else:
                    if i+j == 4:
                        return True
    else:
        return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    raise NotImplementedError


def minimax(board):
    is_max = player(board) == X
    best_value = math.inf * (-1 if is_max else 1)
    for move in actions(board):
        value = minmaxvalue(result(board,move),is_max,1)
        if (value > best_value and is_max) or (value < best_value and not is_max):
            action = move
            print(value,"in", action, "is better than",best_value)
            print("Is max?",is_max)
            best_value = value
    print("DECIDED ON ACTION:",action,"WITH VALUE:",best_value)
    return action


def minmaxvalue(board,is_max,depth):
    value = 0
    if terminal(board):
        return utility(board)
    values = []
    for action in actions(board):
        depth += 1
        value += minmaxvalue(result(board,action),not is_max,depth)
        depth -= 1
    value += -depth if is_max else depth
    return value