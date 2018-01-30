import textwrap


def feedbackReview(feedback, size):
    return textwrap.wrap(feedback, size)


print(feedbackReview("This is an example feedback", 8) == ["This is",
                                                           "an",
                                                           "example",
                                                           "feedback"])
print(feedbackReview("This is an example feedback", 40)
      == ["This is an example feedback"])
print(feedbackReview("", 10) == [])
print(feedbackReview("Dude, do you even review these feedbacks?", 16) == ["Dude, do you",
                                                                          "even review",
                                                                          "these feedbacks?"])
