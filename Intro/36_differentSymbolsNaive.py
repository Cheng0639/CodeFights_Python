def differentSymbolsNaive(s):
    return len(set(s))

print(differentSymbolsNaive("cabca") == 3)
print(differentSymbolsNaive("aba") == 2)
