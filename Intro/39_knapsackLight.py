def knapsackLight(value1, weight1, value2, weight2, maxW):
    if (maxW >= weight1 + weight2):
        return value1 + value2
    elif(maxW >= weight1 and maxW >= weight2):
        return max(value1, value2)
    elif(maxW < weight1 and maxW >= weight2):
        return value2
    elif(maxW < weight2 and maxW >= weight1):
        return value1
    else: 
        return 0



print(knapsackLight(10, 5, 6, 4, 8) == 10)
print(knapsackLight(10, 5, 6, 4, 9) == 16)
print(knapsackLight(5, 3, 7, 4, 6) == 7)
print(knapsackLight(10, 2, 11, 3, 1) == 0)