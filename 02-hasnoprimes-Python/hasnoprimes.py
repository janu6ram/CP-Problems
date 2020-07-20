# Write the function hasnoprimes(L) that takes a 2d list L of integers,
# and returns True if L does not contain any primes, and False otherwise.


def fun_hasnoprimes(l):
    for i in l:
        for j in i:
            if not is_prime(j):
                return True
    return False


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True
