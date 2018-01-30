def avoidObstacles(inputArray):
    rlt = 2

    while(any(map(lambda x: x % rlt == 0, inputArray))):
        rlt += 1

    return rlt


print(avoidObstacles([5, 3, 6, 7, 9]) == 4)
print(avoidObstacles([2, 3]) == 4)
print(avoidObstacles([1, 4, 10, 6, 2]) == 7)
