def arrayChange(inputArray):
    cnt = 0
    for i in range(1, len(inputArray)):
        if(inputArray[i] <= inputArray[i - 1]):
            cnt += inputArray[i-1]-inputArray[i]+1
            inputArray[i] = inputArray[i - 1] + 1

    return cnt


print(arrayChange([1, 1, 1]) == 3)
print(arrayChange([-1000, 0, -2, 0]) == 5)
print(arrayChange([2, 1, 10, 1]) == 12)
