with open("input.txt", "r") as f:
    p = lambda d, c, i: d.replace("\n", "").replace(" ", "").split(c)[i]
    print(
        sum(
            [
                (p(d, ":", 1)[int(p(p(d, ":", 0), "-", 0)) - 1] is p(d, ":", 0)[-1])
                ^ (
                    p(d, ":", 1)[int(p(p(d, ":", 0), "-", -1)[:-1]) - 1]
                    is p(d, ":", 0)[-1]
                )
                for d in f.readlines()
            ]
        )
    )
