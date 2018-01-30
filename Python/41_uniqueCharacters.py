def uniqueCharacters(document):
    return sorted(set(document), key=ord)


print(uniqueCharacters("Todd told Tom to trot to the timber") == [" ",
                                                                  "T",
                                                                  "b",
                                                                  "d",
                                                                  "e",
                                                                  "h",
                                                                  "i",
                                                                  "l",
                                                                  "m",
                                                                  "o",
                                                                  "r",
                                                                  "t"])
print(uniqueCharacters("Brilliant, because bacon bites beat bruschetta") == [" ",
                                                                             ",",
                                                                             "B",
                                                                             "a",
                                                                             "b",
                                                                             "c",
                                                                             "e",
                                                                             "h",
                                                                             "i",
                                                                             "l",
                                                                             "n",
                                                                             "o",
                                                                             "r",
                                                                             "s",
                                                                             "t",
                                                                             "u"])
print(uniqueCharacters("Veni, Vidi, Vici") == [" ",
                                               ",",
                                               "V",
                                               "c",
                                               "d",
                                               "e",
                                               "i",
                                               "n"])
