def sortCodefighters(codefighters):
    res = [CodeFighter(*codefighter) for codefighter in codefighters]
    res.sort(reverse=True)
    return list(map(str, res))


class CodeFighter(object):
    def __init__(self, username, id, xp):
        self.username = username
        self.id = int(id)
        self.xp = int(xp)

    def __lt__(self, other):
        return self.id > other.id if self.xp == other.xp else self.xp < other.xp

    def __str__(self):
        return "(user name = {name}, id = {id}, xp = {xp})".format(name=self.username, id=self.id, xp=self.xp)


print(sortCodefighters([["warrior", "1", "1050"],
                        ["Ninja!", "21", "995"],
                        ["recruit", "3", "995"]]))

# print(sortCodefighters([["Na", "59", "3"],
#                         ["Huey", "5", "2"],
#                         ["Elizabeth", "46", "8"],
#                         ["Kelsi", "25", "7"],
#                         ["Myrtice", "53", "2"],
#                         ["Gene", "44", "3"],
#                         ["Season", "77", "4"],
#                         ["James", "20", "9"],
#                         ["Kandy", "86", "1"],
#                         ["Charise", "54", "10"],
#                         ["Lanita", "91", "1"],
#                         ["Jessie", "85", "4"],
#                         ["Shantelle", "60", "6"],
#                         ["Shad", "9", "5"],
#                         ["Doretha", "68", "1"],
#                         ["Jung", "57", "5"],
#                         ["Linwood", "19", "8"],
#                         ["Brynn", "2", "4"],
#                         ["Lupe", "33", "2"],
#                         ["Wilfred", "66", "10"]]))
