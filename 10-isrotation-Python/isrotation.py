# isRotation(x, y) [15 pts]
# Write the function isRotation(x, y) that takes two non-negative integers x and y, both
# guaranteed to not contain any 0's, and
# returns True if x is a rotation of the digits of y and False otherwise. For example,
# 3412 is a rotation of 1234. Any number
# is a rotation of itself.

def isrotation(x, y):
    # Your code goes here
    if x == y:
        return True
    if digit_count(x) != digit_count(y):
        return False
    num = digit_count(x)
    large = pow(10, num-1)

    for i in range(num):
        first = x//large
        remove = x - first * large
        new = remove * 10 + first
        print(new)
        if new == y:
            return True
        x = new
    return False


def digit_count(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    return count


isrotation(12345, 54321)
