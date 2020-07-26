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
    print(ugly_numbers)
    return ugly_numbers[n]


def prime_factors(n):
    for i in range(2, n+1, 1):
        while n % i == 0:
            if not is_prime_factor(i):
                return False
            n //= i
    return True


def is_prime_factor(n):
    if n == 2 or n == 3 or n == 5:
        return True
    return False


print(fun_nth_uglynumber(10))
