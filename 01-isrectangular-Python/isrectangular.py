# Write the function isrectangular(L) that takes a possibly-2d
# list L and returns True  if it is rectangular, so each row has
#  the same number of elements. Return False otherwise.


def fun_isrectangular(l):
    t = len(l[0])
    for i in l:
        if len(i) != t or len(i) == len(l):
            return False
    return True


print(fun_isrectangular([[1, 2, 3], [2, 3, 4], [3, 4, 5]]))
