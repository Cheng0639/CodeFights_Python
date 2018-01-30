class Prizes(object):
    def __init__(self, customers, n, d):
        self.customers = customers
        self.n = n
        self.d = d

    def __iter__(self):
        return iter(i + 1 for i, v in enumerate(self.customers) if (i + 1) %
                    self.n == 0 and v % self.d == 0)


class Prizes1(object):
    def __init__(self, customers, n, d):
        self.customers = customers
        self.n = n
        self.d = d

    def __iter__(self):
        for i, v in enumerate(self.customers):
            if (i + 1) % self.n == 0 and v % self.d == 0:
                yield i + 1


class Prizes2(object):
    def __init__(self, customers, n, d):
        self.winners = [(i + 1) * n for i,
                        v in enumerate(customers[n - 1::n]) if v % d == 0]

    def __iter__(self):
        return iter(self.winners)


class Prizes3(object):
    def __new__(self, customers, n, d):
        return iter((i + 1) * n for i, v in enumerate(customers[n - 1::n]) if v % d == 0)


def superPrize(purchases, n, d):
    return list(Prizes2(purchases, n, d))


print(superPrize([12, 43, 13, 465, 1, 13], 2, 3))

# print(superPrize([12, 43, 13, 465, 1, 13], 2, 3) == [4])
# print(superPrize([], 2, 2) == [])
# print(superPrize([988, 126, 876, 615, 323, 835, 815, 2,
#                   867, 952, 95, 397, 546, 762, 350], 17, 7) == [])
# print(superPrize([41, 51, 91, 72, 71, 30, 28, 35, 55, 62,
#                   65, 45, 100, 54, 83, 69, 66, 43], 2, 5) == [6, 8, 12])
