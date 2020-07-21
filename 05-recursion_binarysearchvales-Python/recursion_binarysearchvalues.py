# recusive binarySearchValues(L, v) [20 pts] [autograded]
# Write the recursive function binarySearchValues(L, v) that takes a sorted list L and a value v and returns a list
# of tuples, (index, value), of the values that binary search must check to verify whether or not v is in L. As an
# example, say:
#    L = ['a', 'c', 'f', 'g', 'm', 'q']
#    v = 'c'
# Binary search always searches between some lo and hi index, which initially are 0 and (len(L)-1). So here, lo=0
# and hi=5. The first index we try, then, is mid=2 (the integer average of lo and hi). The value there is 'f', so we
# will add (2, 'f') to our result.
# Since 'f' is not the value we are seeking, we continue, only now we are searching from lo=0 to hi=1 (not hi=2
# because we know that index 2 was too high!).
# Now we try mid=0 (the integer average of lo and hi), and so we add (0, 'a') to our result.
# We see that 'a' is too low, so we continue, only now with lo=1 and hi=1. So we add (1, 'c') to our result. We
# found 'c', so we're done. And so we see:
#     L = ['a', 'c', 'f', 'g', 'm', 'q']
#     v = 'c'
#     assert(binarySearchValues(L, v) == [(2,'f'), (0,'a'), (1,'c')])
# Hint: Do not slice the list L, but rather adjust the indexes into L.

def recursion_binarysearchvalues(L, v):
    # Your codes goes here
    low = 0
    if type(L[-2]) == int:
        low = L[-2]
    high = len(L)-1
    if type(L[-1]) == int:
        high = L[-1]
    L.pop(-1)
    L.pop(-1)
    print(L)
    if low > high:
        return []
    mid = low + (high-low)//2
    tup = (mid, L[mid])
    arr = [tup]
    if L[mid] == v:
        return arr
    if v > L[mid]:
        low = mid+1
    else:
        high = mid-1
    if type(L[-1]) == int:
        L[-1] = high
        L[-2] = low
    else:
        L.append(low)
        L.append(high)
    return arr + recursion_binarysearchvalues(L, v)


print(recursion_binarysearchvalues(['a', 'c', 'f', 'g', 'm', 'q'], 'a'))
