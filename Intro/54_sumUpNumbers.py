import re


def sumUpNumbers(inputString):
    return sum(map(int, re.findall("\d+", inputString)))


print(sumUpNumbers("2 apples, 12 oranges") == 14)
print(sumUpNumbers("123450") == 123450)
print(sumUpNumbers("Your payment method is invalid") == 0)
