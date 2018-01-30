def fibonacciGenerator(n):
    def fib():
        last = (0, 1)
        while True:
            yield last[0]
            last = last[0] + last[1], last[0]

    gen = fib()
    return [next(gen) for _ in range(n)]


print(fibonacciGenerator(3) == [0, 1, 1])
print(fibonacciGenerator(1) == [0])
print(fibonacciGenerator(7) == [0, 1, 1, 2, 3, 5, 8])
