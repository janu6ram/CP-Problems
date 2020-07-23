# Pool balls are arranged in balls where the first row contains 1 pool ball and each row contains 1
# more pool ball than the previous row.
# numberOfPoolBallRows(balls) that takes a non-negative int number of pool balls, and returns the
# smallest int number of balls required for the given number of pool balls. Thus, numberOfPoolBallRows(6)
# returns 3. Note that if any balls must be in a row, then you count that row, and so
# numberOfPoolBallRows(7) returns 4 (since the 4th row must have a single ball in it).
import math

# sum of n terms is n(n+1)/2. so  equate n(n+1) = 2 * balls then
# we get quadratic equation will be n**2 + n - 2(balls) =0


def fun_numberofpoolballrows(balls):
    c = -2 * balls
    det = (1) - (4 * c)
    rows = (-1 + math.sqrt(det))/2
    # print(math.ceil(rows))
    return math.ceil(rows)


fun_numberofpoolballrows(0)
