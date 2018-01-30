import math


def tryFunctions(x, functions):
    return [eval(func)(x) for func in functions]


print(tryFunctions(1, ["math.sin",
                       "math.cos",
                       "lambda x: x * 2",
                       "lambda x: x ** 2"]) == [0.84147, 0.5403, 2, 1])
print(tryFunctions(-20, ["abs"]) == [20])
print(tryFunctions(3, ["math.factorial",
                       "math.exp",
                       "lambda x: 2 ** x"]) == [6, 20.0855369232, 8])
