# Write the function matrixMultiply(m1, m2) that takes two 2d lists
# (that we will consider to be matrices) and returns a new 2d list that
# is the result of multiplying the two matrices. Return None if the
# two matrices cannot be multiplied for any reason.


def fun_matrixmultiply(m1, m2):
    if not validate_matrix(m1) or not validate_matrix(m2):
        return None
    if not is_multiply(m1, m2):
        return None
    mul = []
    for k in range(len(m1)):
        row_mul = []
        for i in range(len(m2[0])):
            sum = 0
            for j in range(len(m2)):
                sum += (m1[k][j] * m2[j][i])
            row_mul.append(sum)
        mul.append(row_mul)
    print(mul)
    return mul


def is_multiply(m1, m2):
    if len(m1[0]) == len(m2):
        return True
    return False


def validate_matrix(m):
    l = len(m[0])
    for i in m:
        if len(i) != l:
            return False
    return True


fun_matrixmultiply([[1, 3], [2, 4], [2, 5]], [[1, 3, 2, 2], [2, 4, 5, 1]])
