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
    xAmount = 0
    oAmount = 0
    for i in board:
        for j in i:
            if j == X:
                xAmount += 1
            if j == O:
                oAmount += 1
    if xAmount > oAmount:
        return O
    elif oAmount == xAmount:
        return X
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    resultset = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                resultset.add((i,j))

    return resultset
                
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    boardDeepCopy = copy.deepcopy(board)
    i = action[0]
    j = action[1]
    boardDeepCopy[i][j] = player(board)
    return boardDeepCopy
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
    bestValue = math.inf * (-1 if is_max else 1)
    for move in actions(board):
        value = minmaxvalue(result(board,move),is_max)
        if (value > bestValue and is_max) or (value < bestValue and not is_max):
            action = move
            #print(value,"in", action, "is better than",bestValue)
            bestValue = value
    #print("DECIDED ON ACTION:",action,"WITH VALUE:",bestValue)
    return action


# def minmaxvalue(board,ismax):
#     value = 0
#     if terminal(board):
#         return utility(board)
#     values = [minmaxvalue(result(board,action),not ismax) for action in actions(board)]
#     values = sorted(values)
#     bestValue = max(values) if ismax else min(values)
#     print(bestValue)
#     return bestValue

# def minmaxvalue(board,ismax,depth):
#     value = 0
#     if terminal(board):
#         return utility(board)
#     for action in actions(board):
#         depth += 1
#         value += minmaxvalue(result(board,action),not ismax,depth)
#         depth -= 1
#     print(value,value-depth)
#     return value-depth


def minmaxvalue(board,ismax,depth):
    value = 0
    if terminal(board):
        return utility(board)
    values = []
    for action in actions(board):
        values.append(minmaxvalue(result(board,action),not ismax))
    best_value = max(values) if ismax else min(values)
    print(values,best_value,ismax)
    return best_value