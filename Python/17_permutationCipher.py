import string


def permutationCipher(password, key):
    table = str.maketrans(string.ascii_lowercase, key)
    return password.translate(table)


print(permutationCipher("iamthebest", "zabcdefghijklmnopqrstuvwxy") == "hzlsgdadrs")
print(permutationCipher("codefightsrocks",
                        "ebtyfkudagizxmvcnojqwlsrhp") == "tvyfkaudqjovtij")
print(permutationCipher("supersecurepassword",
                        "felkjmwchynzgobvadtipqrxsu") == "tpvjdtjlpdjvfttrbdk")
print(permutationCipher("myprivatestuff",
                        "mvdwjsphaqufinryoltxcgkzbe") == "ibylagmxjtxcss")
print(permutationCipher("x", "abcdefghijklmnopqrstuvwxyz") == "x")