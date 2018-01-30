from itertools import dropwhile


def memoryPills(pills):
    gen = dropwhile(lambda x: len(x) % 2 == 1, pills+['']*3)
    next(gen)
    return [next(gen) for _ in range(3)]


print(memoryPills(["Notforgetan",
                   "Antimoron",
                   "Rememberin",
                   "Bestmedicen",
                   "Superpillsus"]) == ["Bestmedicen",
                                        "Superpillsus",
                                        ""])
print(memoryPills(["Pillin"]) == ["", "", ""])
