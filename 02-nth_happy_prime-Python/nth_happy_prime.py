# A happy prime is a number that is both happy and prime.
# Write the function nthHappyPrime(n) which takes a non-negative integer
# and returns the nth happy prime number (where the 0th happy prime number is 7).


def fun_nth_happy_prime(n):
    list1 = []
    i = 1
    while len(list1) != (n+1):
        if isPrimeNumber(i) and isHappyNumber(i):
            list1.append(i)
        i += 1
    return list1[n]


def isPrimeNumber(n):
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
        i = i+6
        print("i", i)
    return True


def isHappyNumber(n):
    if n == 1:
        return True
    if n == 4 or n <= 0:
        return False
    sum = 0
    while n != 0:
        rem = n % 10
        sum = sum + rem**2
        n = n//10
    print(sum)
    return isHappyNumber(sum)


print(fun_nth_happy_prime(0))
