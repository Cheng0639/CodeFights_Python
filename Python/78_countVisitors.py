class Counter(object):
    def __init__(self, beta_count):
        self.value = beta_count

    def inc(self):
        self.value += 1

    def get(self):
        return self.value


def countVisitors(beta, k, visitors):
    counter = Counter(beta)
    for visitor in visitors:
        if visitor >= k:
            counter.inc()
    return counter.get()
