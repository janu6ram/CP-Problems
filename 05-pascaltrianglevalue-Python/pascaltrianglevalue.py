# Write the function pascalsTriangleValue(row, col)
# that takes int values row and col, and returns the
# value in the given row and column of Pascal's
# Triangle where the triangle starts at row 0, and
# each row starts at column 0. If either row or col
# are not legal values, return None, instead of crashing.


def fun_pascaltrianglevalue(row, col):
    if col > row + 1:
        return 0
    value = 1
    if col > row-col:
        col = row-col
    for i in range(0, col):
        value = value * (row - i)
        value = value//(i + 1)
    return value
