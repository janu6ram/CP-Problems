# longestDigitRun(n) [20 pts]
# Write the function longestDigitRun(n) that takes a possibly-negative int value n and returns
# the digit that has the longest consecutive
# run, or the smallest such digit if there is a tie. So, longestDigitRun(117773732) returns 7 (
# because there is a run of 3 consecutive 7's),
# as does longestDigitRun(-677886).
import sys


def longestdigitrun(n):
    # Your code goes here
    count = 1
    max1 = 0
    n = abs(n)
    prev = sys.maxsize
    while n != 0:
        rem1 = n % 10
        n //= 10
        rem2 = n % 10
        if rem1 == rem2:
            count += 1
            if count >= max1 and rem1 <= prev:
                max1 = count
                prev = rem1
        else:
            count = 1
    print(max1, prev)
    return prev


longestdigitrun(-677886)
