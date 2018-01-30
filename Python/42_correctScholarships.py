def correctScholarships(bestStudents, scholarships, allStudents):
    return set(bestStudents) <= set(scholarships) < set(allStudents)


def correctScholarships1(bestStudents, scholarships, allStudents):
    return len(scholarships) != len(allStudents) and all(map(lambda x: x in scholarships and x in allStudents, bestStudents)) and all(map(lambda x: x in allStudents, scholarships))


print(correctScholarships([3, 5], [3, 5, 7], [1, 2, 3, 4, 5, 6, 7]))
