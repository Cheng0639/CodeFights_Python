def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        return upperBound

    return found


print(mexFunction([0, 4, 2, 3, 1, 7], 10) == 5)
print(mexFunction([0, 4, 2, 3, 1, 7], 3) == 3)
print(mexFunction([], 13) == 0)
print(mexFunction([1, 5, 10, 20, 4, 11, 18, 0, 9,
                   3, 8, 15, 19, 16, 17, 7, 13, 2, 14], 18) == 6)
print(mexFunction([60, 81, 54, 10, 70, 56, 9, 7, 38, 43, 49, 33, 45, 52, 75, 26, 59, 19, 35, 12, 30, 36, 41, 79,
                   6, 53, 24, 63, 5, 20, 76, 62, 34, 78, 67, 8, 18, 2, 1, 25, 42, 69, 17, 50, 57, 28, 80, 39, 77, 51], 47) == 0)
