import re


def longestWord(text):
    return sorted(re.split("\W+", text), key=lambda x: len(x))[-1]


print(longestWord("Ready, steady, go!") == "steady")
print(longestWord("Ready[[[, steady, go!") == "steady")
print(longestWord("ABCd") == "ABCd")
