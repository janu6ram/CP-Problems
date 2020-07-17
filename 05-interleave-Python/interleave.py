# Write the function interleave(s1, s2) that takes two strings, s1 and s2,
# and interleaves their characters starting with the first character in s1.
# For example, interleave('pto', 'yhn') would return the string "python".
# If one string is longer than the other, concatenate the rest of the remaining
# string onto the end of the new string. For example ('a#', 'cD!f2') would return
# the string "ac#D!f2". Assume that both s1 and s2 will always be strings.


def fun_interleave(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    l = min(l1, l2)
    s = ""
    for i in range(l):
        s += s1[i]+s2[i]
    s += s1[l:] + s2[l:]
    print(s)
    return s


fun_interleave('pto', 'yhn')
