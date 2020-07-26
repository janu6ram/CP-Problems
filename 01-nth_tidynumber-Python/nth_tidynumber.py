# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number.
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46
import sys


def fun_nth_tidynumber(n):
    tidy_numbers = []
    i = 1
    while len(tidy_numbers) != n+1:
        if increasing(i):
            tidy_numbers.append(i)
        i += 1
    return tidy_numbers[n]


def increasing(n):
    prev = sys.maxsize
    while n != 0:
        rem = n % 10
        if prev >= rem:
            prev = rem
        else:
            return False
        n //= 10
    return True


print(fun_nth_tidynumber(35))
