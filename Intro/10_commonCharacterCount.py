def commonCharacterCount(s1, s2):
    return sum([min(s1.count(i), s2.count(i))for i in set(s1)])


print(commonCharacterCount("aabcc", "adcaa") == 3)
print(commonCharacterCount("zzzz", "zzzzzzz") == 4)
print(commonCharacterCount("abca", "xyzbac") == 3)
