# Without using the builtin method s.replace(),
# write its equivalent. Specifically, write the function
# replace(s1, s2, s3) that returns a string equal to
# s1.replace(s2, s3), but again without calling s.replace().


def fun_replace(s1, s2, s3):
    l2 = len(s2)
    l3 = len(s3)
    s = ""
    j = 0
    flag = False
    for i in range(len(s1)):
        if(s1[i] == s2[0]):
            if(s2 == s1[i:i+l2]):
                s += s3
                flag = True
        if(flag == True):
            j += 1
            if j == l3:
                flag = False
                j = 0
            continue
        s += s1[i]

    print(s)
    return s


fun_replace("helloworld123", "123", "345")
