def sortStudents(students):
    students.sort(key=lambda s: s.split()[len(s.split()) - 1])
    return students


print(sortStudents(["John Smith",
                    "Jacky Mon Simonoff",
                    "Lucy Smith",
                    "Angela Zimonova"]) == ["Jacky Mon Simonoff",
                                            "John Smith",
                                            "Lucy Smith",
                                            "Angela Zimonova"])
print(sortStudents(["Lucy Smith",
                    "John Smith",
                    "Jacky Mon Simonoff",
                    "Angela Zimonova"]) == ["Jacky Mon Simonoff",
                                            "Lucy Smith",
                                            "John Smith",
                                            "Angela Zimonova"])
print(sortStudents(["Kate"]) == ["Kate"])
print(sortStudents(["Massuginn Dragonbrewer",
                    "Gragrinelynn Chainbasher",
                    "Barirud Treasureforged",
                    "Orimir Rubyheart",
                    "Krathoun Flatbuster",
                    "Museagret Browngrog",
                    "Groodgratelin Magmabuckle"]) == ["Museagret Browngrog",
                                                      "Gragrinelynn Chainbasher",
                                                      "Massuginn Dragonbrewer",
                                                      "Krathoun Flatbuster",
                                                      "Groodgratelin Magmabuckle",
                                                      "Orimir Rubyheart",
                                                      "Barirud Treasureforged"])
print(sortStudents(["Massuginn Dragonbrewer",
                    "Nomneare Windback",
                    "Nurgutrude Strongpike",
                    "Barirud Treasureforged",
                    "Rudrud Lavahelm",
                    "Asseam Coindelver",
                    "Krathoun Flatbuster",
                    "Museagret Browngrog",
                    "Gorbaebelle Brickbelt",
                    "Groodgratelin Magmabuckle"]) == ["Gorbaebelle Brickbelt",
                                                      "Museagret Browngrog",
                                                      "Asseam Coindelver",
                                                      "Massuginn Dragonbrewer",
                                                      "Krathoun Flatbuster",
                                                      "Rudrud Lavahelm",
                                                      "Groodgratelin Magmabuckle",
                                                      "Nurgutrude Strongpike",
                                                      "Barirud Treasureforged",
                                                      "Nomneare Windback"])
