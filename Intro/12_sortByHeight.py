def sortByHeight(a):
    l = sorted([i for i in a if i > 0])
    for n, i in enumerate(a):
        if i == -1:
            l.insert(n, i)
    return l


print(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180])
      == [-1, 150, 160, 170, -1, -1, 180, 190])
print(sortByHeight([-1, -1, -1, -1, -1]) == [-1, -1, -1, -1, -1])
print(sortByHeight([4, 2, 9, 11, 2, 16]) == [2, 2, 4, 9, 11, 16])
