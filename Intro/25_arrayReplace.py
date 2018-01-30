def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if i == elemToReplace else i for i in inputArray]


print(arrayReplace([1, 2, 1], 1, 3) == [3, 2, 3])
print(arrayReplace([1, 2, 3, 4, 5], 3, 0) == [1, 2, 0, 4, 5])
print(arrayReplace([1, 1, 1], 1, 10) == [10, 10, 10])
