import itertools
from functools import reduce
import math

def compose(functions):
    return reduce(lambda x,y:lambda z: x(y(z)), functions)


def functionsComposition(functions, x):
    return compose(map(eval, functions))(x)


print(functionsComposition(["abs",
                            "math.sin",
                            "lambda x: 3 * x / 2"], 3.1415))
print(functionsComposition(["abs",
                            "math.sin",
                            "lambda x: 3 * x / 2"], 3.1415) == 1)
