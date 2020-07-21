# Recursion-Only powersOf3ToN(n) [15 pts]
# Write the function powersOf3ToN(n) that takes a possibly-negative float or int n, and returns a list of the
# positive powers of 3 up to and including n. As an example, powersOf3ToN(10.5) returns [1, 3, 9]. If no such powers
# of 3 exist, you should return the empty list. You may not use loops/iteration in this problem.
import math


def recursion_powersof3ton(n):
    # Your code goes here
    if n < 1:
        return None
    if n == 1:
        return []
    qut = n//3
    x = int(math.pow(3*qut, 1/3))
    return recursion_powersof3ton(qut) + [3**x]


print(recursion_powersof3ton(100))
