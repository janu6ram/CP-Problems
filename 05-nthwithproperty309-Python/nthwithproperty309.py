# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every
# digit (from 0 to 9) at least once. 309 is the smallest number with this property.
# Write the function nthWithProperty309 that takes a non-negative int n and returns
# the nth number with Property309.

def nthwithproperty309(n):
    # Your code goes here
    list1 = []
    i = 309
    while len(list1) != n+1:
        power = pow(i, 5)
        if check_digits(power):
            print(power)
            list1.append(power)
        i += 1
    return list1[n]


def check_digits(n):
    dict1 = {}
    count = 0
    while n != 0:
        rem = n % 10
        n //= 10
        if rem not in dict1:
            dict1[rem] = 1
            count += 1
        else:
            dict1[rem] += 1
    if count == 10:
        return True
    else:
        return False


print(nthwithproperty309(1))
