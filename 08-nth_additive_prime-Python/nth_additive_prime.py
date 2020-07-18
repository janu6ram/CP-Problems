# Write the function fun_nth_additive_prime(n) that takes a non-negative int n
# and returns the nth Additive Prime, which is a prime number such that
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


def fun_nth_additive_prime(n):
    primes = []
    i = 2
    while len(primes) != n+1:
        if prime_number(i) and additive(i):
            primes.append(i)
        i += 1
    print(primes)
    return primes[n]


def prime_number(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i = i + 6
    return True


def additive(n):
    sum = 0
    while n != 0:
        rem = n % 10
        n = n//10
        sum += rem
    if prime_number(sum):
        return True
    else:
        return False


fun_nth_additive_prime(8)
