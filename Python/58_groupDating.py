def groupDating(male, female):
    return [[], []] if male == female else list(zip(*filter(lambda x: x[0] != x[1], zip(male, female))))


print(groupDating([5, 28, 14, 99, 17], [5, 14, 28, 99, 16]) == [[28, 14, 17],
                                                                [14, 28, 16]])
