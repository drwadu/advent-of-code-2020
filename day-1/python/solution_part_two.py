with open("../input.txt", "r") as f:
    print(
        list(
            filter(
                lambda l: bool(l),
                (
                    lambda es: [
                        i * j * k if i + j + k == 2020 else 0
                        for i in es
                        for j in es
                        for k in es
                    ]
                )(list(map(int, f.readlines()))),
            )
        )[0]
    )
