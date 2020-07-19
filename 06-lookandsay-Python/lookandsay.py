# First, you can read about look-and-say numbers here. Then, write the function lookAndSay(a) that takes a list of
# numbers and returns a list of numbers that results from "reading off" the initial list using the look-and-say
# method, using tuples for each (count, value) pair. For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

def lookandsay(a):
    # Your code goes here
    if len(a) == 0:
        return a
    list1 = []
    count = 1
    if len(a) == 1:
        return list1.append((count, a[0]))
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            count += 1
            continue
        list1.append((count, a[i]))
        count = 1
    list1.append((count, a[i+1]))
    return list1


lookandsay([1, 1, 1, 2, 2, 1, 1, 3])
