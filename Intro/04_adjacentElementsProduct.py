def adjacentElementsProduct(inputArray):
    return max([(inputArray[i] * inputArray[i + 1])for i in range(len(inputArray) - 1)])


print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]) == 21)
print(adjacentElementsProduct([-1, -2]) == 2)
print(adjacentElementsProduct([5, 1, 2, 3, 1, 4]) == 6)
print(adjacentElementsProduct([1, 2, 3, 0]) == 6)
