def allLongestStrings(inputArray):
    m = max([len(i) for i in inputArray])
    return [i for i in inputArray if len(i) == m]


print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]) == ["aba",
                                                               "vcd",
                                                               "aba"])
print(allLongestStrings(["a", "abc", "cbd", "zzzzzz", "a",
                         "abcdef", "asasa", "aaaaaa"]) == ["zzzzzz", "abcdef", "aaaaaa"])
