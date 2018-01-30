def pressureGauges(morning, evening):
    return [[ min(i) for i in zip(morning,evening)],[ max(i) for i in zip(morning,evening)]]


print(pressureGauges([3, 5, 2, 6], [1, 6, 6, 6]) == [[1, 5, 2, 6],
                                                     [3, 6, 6, 6]])
print(pressureGauges([0, 12, 478, 23, 1000], [48, 23, 56, 23, 88]) == [[0, 12, 56, 23, 88],
                                                                       [48, 23, 478, 23, 1000]])
