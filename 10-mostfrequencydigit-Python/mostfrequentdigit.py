# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9
# that occurs most frequently in it, with ties going to the smaller digit.

import collections


def mostfrequentdigit(n):
    # your code goes here
    num_st = str(n)
    num_list = list(num_st)
    print(num_list)
    print(collections.Counter(num_list).items())
    repeat = [(count, item)
              for item, count in sorted(collections.Counter(num_list).most_common())]
    if not repeat:
        return int(num_list[0])
    else:
        return int(repeat[0][1])


print(mostfrequentdigit(5231123123123))
