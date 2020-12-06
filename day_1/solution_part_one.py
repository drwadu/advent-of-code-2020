with open("input.txt", "r") as f:
    print(
        (
            lambda entries: list(
                filter(
                    lambda k: k,
                    [
                        i * j if i + j == 2020 and not i == j else 0
                        for i in entries
                        for j in entries
                    ],
                )
            )
        )(list(map(int, f.readlines())))[0]
    )
