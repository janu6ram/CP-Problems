# hasConsecutiveDigits(n)  [10pts]
# Write the function hasConsecutiveDigits(n) that takes a possibly negative int value n and returns True if that
# number contains two consecutive digits that are the same, and False otherwise.

def hasconsecutivedigits(n):
    # your code goes here
    num = abs(n)
    num_st = str(num)
    num_list = list(num_st)
    for i in range(len(num_list)-1):
        if int(num_list[i]) + 1 == int(num_list[i+1]):
            return True
    return False
