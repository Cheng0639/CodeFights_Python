def isTestSolvable(ids, k):
    digitSum = lambda x: sum([ int(i) for i in str(x)])

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0

print( isTestSolvable([529665, 909767, 644200],3)==True)
print( isTestSolvable([505472, 823554, 608771, 106888, 819471, 116625, 689811, 309397, 942937, 902554, 677532, 562522, 145067, 508460, 3501, 293533, 898993, 407738, 156093, 847039, 668357, 645962, 297698, 58190, 781139, 64724, 169176, 239193, 416474, 694882, 974958, 766959, 97136, 788718, 641266, 200950, 468728, 245625, 324219, 311677]
,6)==False)