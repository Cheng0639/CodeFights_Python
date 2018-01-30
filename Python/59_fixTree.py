def fixTree(tree):
    return [i.strip().center(len(i)) for i in tree]


def fixTree1(tree):
    return ["{a:^{b}}".format(a='*' * i.count('*'), b=max(map(len, tree)))for i in tree]


print(fixTree(["      *  ",
               "    *    ",
               "***      ",
               "    *****",
               "  *******",
               "*********",
               " ***     "]) == ["    *    ",
                                 "    *    ",
                                 "   ***   ",
                                 "  *****  ",
                                 " ******* ",
                                 "*********",
                                 "   ***   "])
# print(fixTree(["    *    ",
#                "    *    ",
#                "   ***   ",
#                "  *****  ",
#                " ******* ",
#                "*********",
#                "   ***   "]) == ["    *    ",
#                                  "    *    ",
#                                  "   ***   ",
#                                  "  *****  ",
#                                  " ******* ",
#                                  "*********",
#                                  "   ***   "])
