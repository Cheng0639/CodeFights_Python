def printList(lst):
    return "This is your list: " + str(lst)


def printList1(lst):
    return "This is your list: [{data}]".format(data=", ".join([str(i) for i in lst]))


print(printList([1, 2, 3, 4, 5]) == "This is your list: [1, 2, 3, 4, 5]")
print(printList([]) == "This is your list: []")
print(printList([-74, -71, -7, -88, 13, -22, 7, 7, 71, 28, -
                 78, -17, 77, 10]) == "This is your list: [-74, -71, -7, -88, 13, -22, 7, 7, 71, 28, -78, -17, 77, 10]")
