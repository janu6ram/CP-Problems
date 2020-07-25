# Background: a Kaprekar number is a non-negative integer, the representation of whose square
# can be split into two possibly-different-length parts (where the right part is not zero)
# that add up to the original number again. For instance, 45 is a Kaprekar number, because
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,...
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math


def fun_nth_kaprekarnumber(n):
    kaprekars = []
    i = 1
    while len(kaprekars) != n+1:
        square = pow(i, 2)
        if check_sum(square) == i:
            kaprekars.append(i)
        i += 1
    return kaprekars[n]


def check_sum(n):
    if (1 + int(math.log10(n))) % 2 != 0:
        return n
    right = 0
    p = 0
    while n != 0:
        rem = n % 10
        n //= 10
        right += rem*(10**p)
        if right == 0:
            p += 1
            continue
        print(n, right)
        ll = (1 + int(math.log10(n)))
        rl = (1 + int(math.log10(right)))
        if rem == 0:
            rl += 1
        if ll <= rl:
            return right + n
        p += 1


print(fun_nth_kaprekarnumber(4))
