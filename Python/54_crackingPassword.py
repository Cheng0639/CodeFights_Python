from itertools import product


def crackingPassword1(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))
    return list(sorted([ i for i in map(createNumber, product(digits, repeat=k)) if int(i)%d==0]))


def crackingPassword(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return list(sorted(filter(lambda x: int(x) % d == 0, map(createNumber, product(digits, repeat=k)))))


print(crackingPassword([1, 5, 2], 2, 3) == ["12",
                                            "15",
                                            "21",
                                            "51"])
print(crackingPassword([4, 6, 0, 3], 4, 13,) == ["0000",
                                                 "0364",
                                                 "0403",
                                                 "0663",
                                                 "3003",
                                                 "3406",
                                                 "3640",
                                                 "3666",
                                                 "4004",
                                                 "4030",
                                                 "4043",
                                                 "4303",
                                                 "4433",
                                                 "4446",
                                                 "6006",
                                                 "6344",
                                                 "6604",
                                                 "6630",
                                                 "6643"])
