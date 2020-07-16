# Write the function nthHappyNumber(n) which takes a non-negative integer
# and returns the nth happy number (where the 0th happy number is 1).
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)

from ishappynumber import ishappynumber


def fun_nth_happy_number(n):
    list = []
    i = 1
    while(len(list) != n+1):
        if(ishappynumber(i)):
            list.append(i)
        i += 1
    return list[n]


print(fun_nth_happy_number(3))
