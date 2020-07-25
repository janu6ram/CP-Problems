# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0
# and which remains prime when the leading (left) digit is successively removed.
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime.
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and
# nthLeftTruncatablePrime(10) returns 53.


import math


def fun_nth_lefttruncatableprime(n):
    truncate_primes = []
    i = 2
    while len(truncate_primes) != n+1:
        if prime(i) and truncate_prime(i):
            truncate_primes.append(i)
        i += 1
    return truncate_primes[n]


def truncate_prime(n):
    digits = int(math.log10(n))
    while digits != 0:
        n %= 10**digits
        if not prime(n):
            return False
        digits -= 1
    return True


def prime(n):
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
