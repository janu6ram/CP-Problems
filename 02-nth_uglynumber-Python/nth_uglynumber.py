# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number.
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8,
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.


def fun_nth_uglynumber(n):
    ugly_numbers = []
    i = 1
    while len(ugly_numbers) != n+1:
        if prime_factors(i):
            ugly_numbers.append(i)
        i += 1
    return ugly_numbers[n]


def prime_factors(n):
    for i in range(2, n+1, 1):
        while n % i == 0:
            if not is_prime(i):
                return False
            n //= i
    return True


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
