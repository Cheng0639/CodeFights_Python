def addBorder(picture):
    l = len(picture[0]) + 2
    return ['*' * l] + [i.center(l, '*') for i in picture] + ['*' * l]


print(addBorder(["abc",
                 "ded"]) == ["*****",
                             "*abc*",
                             "*ded*",
                             "*****"])
print(addBorder(["a"]) == ["***",
                           "*a*",
                           "***"])
