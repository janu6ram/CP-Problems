# isSorted(a) (10 Pts)
# Write the function isSorted(a) that takes a list of numbers and returns True if the list
# is sorted (either smallest-first or largest-first) and False otherwise. Your function
# must only consider each value in the list once (so, in terms of big-oh, which we will
# learn soon, it runs in O(n) time, where n=len(a)), and so in particular you may not sort
# the list.

def issorted(a):
    # your code goes here
    less = 0
    more = 0
    for i in range(0, len(a)-1):
        if a[i] <= a[i+1]:
            less += 1
        elif a[i] >= a[i+1]:
            more += 1
            less
    if less == len(a) or more == len(a):
        return True
    else:
        return False


print(issorted([10, 9, 8, 7, 6, 5, 4, 3, 2, 10]))
