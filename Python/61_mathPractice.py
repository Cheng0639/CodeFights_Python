from functools import reduce


def mathPractice(numbers):
    return reduce(lambda x, y: x * y[1] if y[0] % 2 == 0 else x + y[1], enumerate(numbers), 1)


print(mathPractice([1, 2, 3, 4, 5, 6]) == 71)
print(mathPractice([8, 9]) == 17)
print(mathPractice([0, 8, 15]) == 120)
