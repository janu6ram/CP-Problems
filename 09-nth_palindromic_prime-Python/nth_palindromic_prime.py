# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n
# and returns the nth palindromic Prime, which is a palidrome number such that
# it is also a prime. For example, 313 is a palindrome and it is prime
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2


def fun_nth_palindromic_prime(n):
    primes = []
    i = 2
    while len(primes) != n+1:
        if pallindrome(i) and prime_number(i):
            primes.append(i)
        i += 1
    return primes[n]


def pallindrome(n):
    temp = n
    rev = 0
    while temp != 0:
        rem = temp % 10
        temp = temp//10
        rev = rev * 10 + rem
    if rev == n:
        return True
    else:
        return False


def prime_number(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i = i + 6
    return True
# pallindrome(786)
