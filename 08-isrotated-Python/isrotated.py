# isRotated(str1, str2) [10 pts]
# Write an efficient program to test if two given String is a rotation of each other or not, e.g.
# if given String is "XYZ" and "ZXY" then your function should return true, but if the input is
# "XYZ" and "YXZ" then return false.


def isrotated(str1, str2):
    # Your code goes here
    for i in range(len(str1)):
        if str1[i] == str2[0]:
            break
    s = str1[i:] + str1[:i]
    if s == str2:
        return True
    else:
        return False


print(isrotated("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "BCDEFGHIJKLMNOPQRSTUVWXYZA"))
