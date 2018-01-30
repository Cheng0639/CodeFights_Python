def chessTeams(smarties, cleveries):
    return [[smarties[i], cleveries[i]] for i in range(0, len(smarties))]


def chessTeams(smarties, cleveries):
    return list(map(list, (zip(smarties, cleveries))))


print(chessTeams(["Jane",
                  "Bob",
                  "Peter"], ["Oscar",
                             "Lidia",
                             "Ann"]) == [["Jane", "Oscar"],
                                         ["Bob", "Lidia"],
                                         ["Peter", "Ann"]])
print(chessTeams(["Harry",
                  "Hermione",
                  "Ron",
                  "Albus"], ["Draco",
                             "Crabbe",
                             "Goyle",
                             "Tom"]) == [["Harry", "Draco"],
                                         ["Hermione", "Crabbe"],
                                         ["Ron", "Goyle"],
                                         ["Albus", "Tom"]])
