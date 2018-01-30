def deleteDigit(n):
    s = str(n)
    return max([int(s[:i] + s[i + 1:]) for i in range(0, len(s))])


print(deleteDigit(152) == 52)
print(deleteDigit(1001) == 101)
print(deleteDigit(10) == 1)
print(deleteDigit(222219) == 22229)
