def simpleSort(arr):
    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
    return arr


print(simpleSort([2, 4, 1, 5]) == [1, 2, 4, 5])
print(simpleSort([3, 6, 1, 5, 3, 6]) == [1, 3, 3, 5, 6, 6])
print(simpleSort([100]) == [100])
print(simpleSort([-1, -2, 0]) == [-2, -1, 0])
