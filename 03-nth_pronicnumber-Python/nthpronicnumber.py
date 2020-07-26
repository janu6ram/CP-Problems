# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a
# number n is a product of x and (x+1).

def nthpronicnumber(n):
    # Your code goes here
    pronic_numbers = []
    i = 0
    while len(pronic_numbers) != n+1:
        pronic_numbers.append(i * i+1)
        i += 1
    return pronic_numbers[n]


print(nthpronicnumber(0))
