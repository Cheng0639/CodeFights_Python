def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        x, *res, z = res
    return res


print(listBeautifier([3, 4, 2, 4, 38, 4, 5, 3, 2]) == [4, 38, 4])
print(listBeautifier([1, 4, -5]) == [4])
print(listBeautifier([]) == [])
print(listBeautifier([8]) == [8])
print(listBeautifier([10, 2, 10, 9, 7, 3, 8, 5, 3, 2, 8, 7]) == [])
print(listBeautifier(
    [8, 5, 1, 2, 3, 8, 1, 10, 5, 1, 4, 6, 9, 2, 8, 8, 9, 4, 10, 3]) == [8, 1, 10, 5, 1, 4, 6, 9, 2, 8])
