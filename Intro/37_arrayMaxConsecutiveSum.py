def arrayMaxConsecutiveSum(inputArray, k):
    c = m = sum(inputArray[:k])
    for i in range(len(inputArray) - k):
        c = c + inputArray[i + k] - inputArray[i]
        m = max(m, c)

    return m

def arrayMaxConsecutiveSum1(inputArray,k):
    return max( [ sum(inputArray[i:i+k]) for i in range(0,len(inputArray)-k+1)]) 

print(arrayMaxConsecutiveSum([ 2, 3, 5, 1, 6 ], 2) == 8)
print(arrayMaxConsecutiveSum([ 2, 4, 10, 1 ], 2) == 14)
print(arrayMaxConsecutiveSum([ 1, 3, 2, 4 ], 3) == 9)
