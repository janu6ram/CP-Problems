# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth
# Circular prime, which is a prime number that does not contain any 0's and such that all the
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3,
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime,
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

circular_primes = [2]


def nthcircularprime(n):
    # Your code goes here
    while len(circular_primes) != n:
        i = 3
        if isPrime(i) and circular_prime(i):
            circular_primes.append(i)
        i += 2
    print(circular_primes)
    return circular_primes[n-1]


def circular_prime(n):
    while n != 0:
        rem = n % 10
        n //= 10
        if not isPrime(rem):
            return False
    return True


def isPrime(n):
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


print(nthcircularprime(7))
