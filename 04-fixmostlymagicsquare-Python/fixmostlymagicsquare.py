# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic
# square.


def fixmostlymagicsquare(L):
    # Your code goes here
    which_row(L)
    # col,diff = which_col(L)


def which_row(L):
    rows = []
    for i in L:
        sum = 0
        for j in i:
            sum += j
        if sum in rows:
            correct = sum
        rows.append(sum)
    print(rows)


fixmostlymagicsquare([[2, 7, 9], [9, 5, 1], [4, 3, 8]])
