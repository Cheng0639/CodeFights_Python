def wordPower(word):
    num = {i: ord(str.lower(i)) - ord('a') + 1 for i in word}
    print({i: ord(str.lower(i)) - ord('a') + 1 for i in word})
    return sum([num[ch] for ch in word])


print(wordPower("Hello"))
print(list(map(str.lower, [i for i in "ASDASDASD"])))
