# Write the function smallestDifference(a) that takes a list of integers and returns
# the smallest absolute difference between any two
# integers in the list. If the list is empty, return -1. For example:
#       assert(smallestDifference([19,2,83,6,27]) == 4)
# The two closest numbers in that list are 2 and 6, and their difference is 4.
import sys


def smallestdifference(a):
    # Your code goes here
    a.sort()
    diff = 0
    least = sys.maxsize
    print(a)
    for i in range(0, len(a)-1):
        diff = a[i+1] - a[i]
        if(diff) < least:
            least = diff
            print(least)
    print(least)
    return least


smallestdifference([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75])
