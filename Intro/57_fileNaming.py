def fileNaming(names):
    rlt = []
    for i in range(0, len(names)):
        if rlt.count(names[i]) == 0:
            rlt.append(names[i])
        else:
            cnt = 1
            while(rlt.count("{x}({y})".format(x=names[i], y=cnt)) > 0):
                cnt += 1

            rlt.append(names[i] + "({x})".format(x=cnt))

    return rlt


print(fileNaming(["doc",
                  "doc",
                  "image",
                  "doc(1)",
                  "doc"]) == ["doc",
                              "doc(1)",
                              "image",
                              "doc(1)(1)",
                              "doc(2)"])
print(fileNaming(["a(1)",
                  "a(6)",
                  "a",
                  "a",
                  "a",
                  "a",
                  "a",
                  "a",
                  "a",
                  "a",
                  "a",
                  "a"]) == ["a(1)",
                            "a(6)",
                            "a",
                            "a(2)",
                            "a(3)",
                            "a(4)",
                            "a(5)",
                            "a(7)",
                            "a(8)",
                            "a(9)",
                            "a(10)",
                            "a(11)"])
print(fileNaming(["dd",
                  "dd(1)",
                  "dd(2)",
                  "dd",
                  "dd(1)",
                  "dd(1)(2)",
                  "dd(1)(1)",
                  "dd",
                  "dd(1)"]) == ["dd",
                                "dd(1)",
                                "dd(2)",
                                "dd(3)",
                                "dd(1)(1)",
                                "dd(1)(2)",
                                "dd(1)(1)(1)",
                                "dd(4)",
                                "dd(1)(3)"])
