def digitDegree(n):
    cnt = 0
    while(n >= 10):
        n = sum([int(x) for x in str(n)])
        cnt += 1

    return cnt

print(digitDegree(5) == 0)
print(digitDegree(100) == 1)
print(digitDegree(91) == 2)
print(digitDegree(99) == 2)