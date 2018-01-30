def isLucky(n):
    s = str(n)
    pv = len(s) // 2
    return sum(map(int, s[:pv])) == sum(map(int, s[pv:]))


print(isLucky(1230) == True)
print(isLucky(239017) == False)
print(isLucky(134008) == True)
