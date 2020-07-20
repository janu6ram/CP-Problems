# canQueenAttack(qX, qY, oX, oY) [15 pts]
# Given the position of the queen (qX, qY) and the opponent (oX, oY) on a chessboard. The task is to determine
# whether the queen can attack the opponent or not. Note that the queen can attack in the same row, same column and
# diagonally.

def canqueenattack(qR, qC, oR, oC):
    # Your code goes here
    if qR == oR or qC == oC or is_diagonal(qR, qC, oR, oC):
        return True
    return False


def is_diagonal(qr, qc, r, c):
    if right_up(qr, qc, r, c) or right_down(qr, qc, r, c) or left_up(qr, qc, r, c) or left_down(qr, qc, r, c):
        return True
    return False


def right_up(qr, qc, r, c):
    row = qr
    col = qc
    while col != 0:
        if row == r and col == c:
            return True
        row += 1
        col -= 1
    return False


def right_down(qr, qc, r, c):
    row = qr
    col = qc
    while col != 0:
        if row == r and col == c:
            return True
        row -= 1
        col -= 1
    return False


def left_down(qr, qc, r, c):
    row = qr
    col = qc
    while col != 9:
        if row == r and col == c:
            return True
        row -= 1
        col += 1
    return False


def left_up(qr, qc, r, c):
    row = qr
    col = qc
    while col != 9:
        if row == r and col == c:
            return True
        row += 1
        col += 1
    return False
