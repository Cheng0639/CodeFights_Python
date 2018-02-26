class Functions(object):
    @staticmethod
    def sign(x):
        return 1 if x > 0 else 0 if x == 0 else -1


def sign(x):
    return Functions.sign(x)
