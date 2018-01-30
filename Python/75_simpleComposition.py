import math
import string
import re
import random
import functools


def compose(f, g):
    return lambda x: f(g(x))


def simpleComposition(f, g, x):
    return compose(eval(f), eval(g))(x)


print(simpleComposition("math.log10", "abs", -100))
print(simpleComposition("math.log10", "abs", -100) == 2)
print(simpleComposition("math.sin", "math.cos", 34.4) == -0.834717445664)

