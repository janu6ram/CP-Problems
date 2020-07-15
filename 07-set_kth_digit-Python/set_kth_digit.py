# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative
# single digit (between 0 and 9 inclusive). This function returns the number n with
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left,
# so the 0th digit is the rightmost digit.


def fun_set_kth_digit(n, k, d):
    np = abs(n)
    st = str(np)
    n_list = list(st)
    if k == len(n_list):
        n_list = [d+""] + n_list
    else:
        n_list[-1-k] = str(d)
    s = ""
    num = s.join(n_list)
    numInt = int(num)
    return numInt
