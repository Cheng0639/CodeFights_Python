def findEmailDomain(address):
    return address[address.rindex('@') + 1:]


print(findEmailDomain("prettyandsimple@example.com") == "example.com")
print(findEmailDomain("<>[]:,;@\"!#$%&*+-/=?^_{}| ~.a\"@example.org") == "example.org");
print(findEmailDomain("someaddress@yandex.ru") == "yandex.ru")
print(findEmailDomain("\" \"@xample.org") == "xample.org")
