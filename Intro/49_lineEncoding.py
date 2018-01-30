from itertools import groupby


def lineEncoding(s):
    x = ''
    print(list(groupby(s)))
    for k, g in groupby(s):
        y = len((list(g)))
        if y == 1:
            x += k
        else:
            x += str(y) + k
    return x


print(lineEncoding("aabbbc") == "2a3bc")
print(lineEncoding("abbcabb") == "a2bca2b")
print(lineEncoding("abcd") == "abcd")
