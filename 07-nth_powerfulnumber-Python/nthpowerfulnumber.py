# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it.
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.

import math


def nthpowerfulnumber(n):
    # Your code goes here
    powerful = []
    i = 1
    while len(powerful) != n+1:
        if check_factors(i):
            powerful.append(i)
        i += 1
    return powerful[n]


# def check_factors


def prime_factors(n):
    factors = set([1])
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, n+1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(2)
    return factors


print(prime_factors(8))
