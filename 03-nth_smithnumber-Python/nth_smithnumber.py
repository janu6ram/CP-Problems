# Write the function nthSmithNumber that takes a non-negative int n
# and returns the nth Smith number, where a Smith number is a composite (non-prime)
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1).
# Note that if a prime number divides the Smith number multiple times, its digit sum
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

import math


def fun_nth_smithnumber(n):
    smith_numbers = []
    i = 4
    while len(smith_numbers) != n+1:
        if (not prime_number(i)) and factors_sum(i) == digit_sum(i):
            smith_numbers.append(i)
        i += 1
    return smith_numbers[n]


def prime_number(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True


def factors_sum(n):
    i = 2
    add = 0
    while i < n:
        if prime_number(i) and n % i == 0:
            add += i
        i += 1
    x = int(math.sqrt(n))
    if x * x == n:
        add += x
    add = digit_sum(add)
    return add


def digit_sum(n):
    add = 0
    while n != 0:
        rem = n % 10
        n //= 10
        add += rem
    return add


print(fun_nth_smithnumber(1))
