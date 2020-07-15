# Write the function getKthDigit(n, k) that takes
# a possibly-negative int n and a non-negative int k,
# and returns the kth digit of n, starting from 0, counting from the right.
# if the kth digit is not present return 0


def fun_get_kth_digit(digit, k):
    dig = abs(digit)
    st = str(dig)
    dig_list = list(st)
    if k >= len(dig_list):
        return 0
    return int(dig_list[-1-k])
