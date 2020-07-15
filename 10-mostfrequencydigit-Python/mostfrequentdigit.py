# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9
# that occurs most frequently in it, with ties going to the smaller digit.

import collections


def mostfrequentdigit(n):
    # your code goes here
    num_st = str(n)
    num_list = list(num_st)
    repeat = [(item, count)
              for item, count in collections.Counter(num_list).items() if count > 1]
    if not repeat:
        return int(num_list[0])
    else:
        return int(repeat[0][0])


print(mostfrequentdigit(5312312355565))
