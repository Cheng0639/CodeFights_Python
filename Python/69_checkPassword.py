def checkPassword(attempts, password):
    def check():
        while True:
            val = yield
            yield val == password

    checker = check()
    for i, attempt in enumerate(attempts):
        next(checker)
        if checker.send(attempt):
            return i + 1

    return -1


print(checkPassword(["hello",
                     "world",
                     "I",
                     "like",
                     "coding"], 'like') == 4)
print(checkPassword(["hello",
                     "world",
                     "I",
                     "like",
                     "coding"], 'qwerty123') == -1)
print(checkPassword(["codefights"], 'codefights') == 1)
print(checkPassword(["123",
                     "456",
                     "qwerty",
                     "zzz",
                     "password",
                     "genius239",
                     "password"], "password") == 5)
