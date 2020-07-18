# Given a string str and an integer K, the task is to find the K-th most
# frequent character in the string. If there are multiple characters that
# can account as K-th the most frequent character then, print any one of them.


def fun_kth_occurrences(s, n):
    dict1 = {}
    for i in s:
        if i == " ":
            dict1 = {}
            continue
        if i in dict1:
            dict1[i] += 1
            if dict1[i] == n+1:
                return i
        else:
            dict1[i] = 1
    return s.strip()[0]
