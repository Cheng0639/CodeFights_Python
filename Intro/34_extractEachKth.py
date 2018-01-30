def extractEachKth(inputArray, k):
    return [v for i, v in enumerate(inputArray) if (i+1) % k != 0]


print(extractEachKth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)== [1, 2, 4, 5, 7, 8, 10])
print(extractEachKth([1, 1, 1, 1, 1], 1) == [])
print(extractEachKth([1, 2, 1, 2, 1, 2, 1, 2], 3) == [1, 1, 1, 1])
