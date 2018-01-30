def collegeCourses(x, courses):
    def shouldConsider(course):
        return len(course) != x

    return list(filter(shouldConsider, courses))


print(collegeCourses(7, ["Art",
                         "Finance",
                         "Business",
                         "Speech",
                         "History",
                         "Writing",
                         "Statistics"]) == ["Art",
                                            "Business",
                                            "Speech",
                                            "Statistics"])
