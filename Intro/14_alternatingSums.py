def alternatingSums(a):
    return [sum(a[::2]), sum(a[1::2])]


print(alternatingSums([50, 60, 60, 45, 70]) == [180, 105])
print(alternatingSums([100, 50]) == [100, 50])
print(alternatingSums([80]) == [80, 0])
