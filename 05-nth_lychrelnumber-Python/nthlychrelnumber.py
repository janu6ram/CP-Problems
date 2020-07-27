# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….


def nthlychrelnumbers(n):
    # your code goes here
    lychrel_numbers = []
    i = 1
    while len(lychrel_numbers) != n:
        if lychrel(i):
            lychrel_numbers.append(i)
        i += 1
    return lychrel_numbers[n-1]


def lycheral(n):
    i = 0
    while not palindrome(n):
        n += reverse(n)
        i += 1
        if i == 30:
            return True
    return False


def palindrome(n):
    rev = reverse(n)
    print(n, rev)
    if n == rev:
        return True
    else:
        return False


def reverse(n):
    rev = 0
    while n != 0:
        rem = n % 10
        n //= 10
        rev = 10*rev + rem
    print(rev)
    return rev


print(lycheral(196))
