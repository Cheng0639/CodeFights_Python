from itertools import permutations


def rockPaperScissors(players):
    return list([i,j] for i , j in sorted(permutations(players, 2)))


print(rockPaperScissors(["trainee",
                         "warrior",
                         "ninja"]) == [["ninja", "trainee"],
                                       ["ninja", "warrior"],
                                       ["trainee", "ninja"],
                                       ["trainee", "warrior"],
                                       ["warrior", "ninja"],
                                       ["warrior", "trainee"]])
print(rockPaperScissors(["Harry",
                         "Ron",
                         "Hermione",
                         "Draco",
                         "Tom"]) == [["Draco", "Harry"],
                                     ["Draco", "Hermione"],
                                     ["Draco", "Ron"],
                                     ["Draco", "Tom"],
                                     ["Harry", "Draco"],
                                     ["Harry", "Hermione"],
                                     ["Harry", "Ron"],
                                     ["Harry", "Tom"],
                                     ["Hermione", "Draco"],
                                     ["Hermione", "Harry"],
                                     ["Hermione", "Ron"],
                                     ["Hermione", "Tom"],
                                     ["Ron", "Draco"],
                                     ["Ron", "Harry"],
                                     ["Ron", "Hermione"],
                                     ["Ron", "Tom"],
                                     ["Tom", "Draco"],
                                     ["Tom", "Harry"],
                                     ["Tom", "Hermione"],
                                     ["Tom", "Ron"]])
