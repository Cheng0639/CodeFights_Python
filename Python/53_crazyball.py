from itertools import combinations


def crazyball(players, k):
    print(list(map(list,(combinations(sorted(players), k)))))
    return list(map(list,(combinations(sorted(players), k))))


print(crazyball(["Ninja",
                 "Warrior",
                 "Trainee",
                 "Newbie"], 3) == [["Newbie", "Ninja", "Trainee"],
                                   ["Newbie", "Ninja", "Warrior"],
                                   ["Newbie", "Trainee", "Warrior"],
                                   ["Ninja", "Trainee", "Warrior"]])
