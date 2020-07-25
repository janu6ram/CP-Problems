# Note: please do not start this problem prior to completing previous problem.
# Bearing in mind the definition of Kaprekar Number from above problem, write the function
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45,
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number,
# nearestKaprekarNumber(50) returns 45.
# Note: as you probably guessed, this also cannot be solved by counting up from 0,
# as that will not be efficient enough to get past the autograder.
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math

def fun_nearestkaprekarnumber(n):
    i = 0
    while True:
        if n-i >= 1 and check_kap(n-i):
            return n-i
        elif check_kap(n+i):
            return n + i
        i += 1

def check_kap(n):
    square = pow(n,2)
    if square < 10 and  square == n:
        return True
    right = 0
    p = 0
    while square != 0:
        rem = square % 10
        square //= 10
        right += rem * (10**p)
        if right + square == n and right != 0 and square != 0:
            return True
        p += 1
    return False
fun_nearestkaprekarnumber(51)