# getallPermutations(str) [20 pts]
# Write an efficient program to print all permutations of a given String. For example, if given input is "abc" then
# your program should print all 6 permutations e.g. [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
import math


def getallpermutations(x):
    # Your code goes here
    length = len(x)
    chars = list(x)
    permutations = []
    factorial = math.factorial(length)
    for i in range(factorial):
        dup = chars.copy()
        n = 1
        list1 = [0] * length
        while i != 0:
            rem = i % n
            list1[length - n] = rem
            i //= n
            n += 1
        print(list1, dup)
        tup = []
        for i in list1:
            tup.append(dup.pop(i))
        permutations.append(tuple(tup))
    print(permutations)
    return permutations


getallpermutations("abc")
