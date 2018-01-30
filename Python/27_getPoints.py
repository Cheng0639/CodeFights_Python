def getPoints(answers, p):
    def questionPoints(i, ans): return (i + 1 if ans else -p)


print(getPoints([True, True, False, True], 2) == 5)
print(getPoints([True, False, True, False], 7) == -10)
print(getPoints([True, False], 0) == 1)
print(getPoints([True, True, True, False, True, True,
                 True, False, True, True, True, True, False], 2) == 60)
print(getPoints([False, True, True, True, False, True], 1) == 13)
print(getPoints([False], 10) == -10)
