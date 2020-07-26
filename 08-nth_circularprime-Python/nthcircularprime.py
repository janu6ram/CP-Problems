# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth
# Circular prime, which is a prime number that does not contain any 0's and such that all the
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3,
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime,
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).

circular_primes = [2]


def nthcircularprime(n):
    # Your code goes here
    while len(circular_primes) != n+1:
        i = 3
        if circular_prime(i):
            circular_primes.append(i)
        i += 2
    return circular_primes[n]
