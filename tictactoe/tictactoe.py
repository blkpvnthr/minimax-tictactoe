"""
Tic Tac Toe Player
"""

import math
import copy

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
    countX = 0
    countO = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countX += 1
            if board[row][col] == O:
                countO += 1
    if countX > countO:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    allPossibleActions = set()

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                allPossibleActions.add((row, col))

    return allPossibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("not valid action")

    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy


def checkCol(board, player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True


def checkRow(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True


def checkFirstDig(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count += 1
        if count == 3:
            return True
        else:
            return False


def checkSecondDig(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1
        if count == 3:
            return True
        else:
            return False


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if checkRow(board, X) or checkCol(board, X) or checkFirstDig(board, X) or checkSecondDig(board, X):
        return X
    if checkRow(board, O) or checkCol(board, O) or checkFirstDig(board, O) or checkSecondDig(board, O):
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    best_action = None
    for action in actions(board):
        min_val = min_value(result(board, action))
        if min_val > v:
            v = min_val
            best_action = action
    if best_action is None:
        return utility(board)
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    best_action = None
    for action in actions(board):
        max_val = max_value(result(board, action))
        if max_val < v:
            v = max_val
            best_action = action
    if best_action is None:
        return utility(board)
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    # Case if player is X (max-player)
    elif player(board) == X:
        best_score = -math.inf
        best_action = None
        # Loop over all the possible actions
        for action in actions(board):
            # Evaluate the score of the resulting board state
            score = min_value(result(board, action))
            # Check if the resulting board is terminal
            if terminal(result(board, action)):
                return action
            # Update the best action if the score is higher than the current best score
            if score > best_score:
                best_score = score
                best_action = action
        return best_action

    # Case if player is O (min-player)
    elif player(board) == O:
        best_score = math.inf
        best_action = None
        # Loop over all the possible actions
        for action in actions(board):
            # Evaluate the score of the resulting board state
            score = max_value(result(board, action))
            # Check if the resulting board is terminal
            if terminal(result(board, action)):
                return action
            # Update the best action if the score is lower than the current best score
            if score < best_score:
                best_score = score
                best_action = action
        return best_action

