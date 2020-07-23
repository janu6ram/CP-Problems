# carry less addition means a  normal addition with the carry from each column ignored.
# So, for example, if we carryless-ly add 8+7, we get 5 (ignore the carry). And if we add
# 18+27, we get 35 (still ignore the carry). With this in mind, write the function
# fun_carrylessadd(x, y) that takes two non-negative integers x and y and returns their
# carryless sum. As the paper demonstrates, fun_carrylessadd(785, 376) returns 51.


def fun_carrylessadd(x, y):
    if x < 0 or y < 0:
        return None
    add = 0
    p = 0
    while x != 0:
        rem = x % 10
        x //= 10
        rem2 = y % 10
        y //= 10
        r = rem + rem2
        r = r % 10
        add += r * (10**p)
        p += 1
    print(add)
    return add


fun_carrylessadd(33, 77)
