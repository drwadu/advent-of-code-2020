with open("input.txt", "r") as f:
    w = list(map(lambda s: s.replace("\n", ""), f.readlines()))
    n = 0; i = 1; j = 3
    while i < len(w):
        s = w[i][: j % len(w[0])]
        if w[i][j % len(w[0])] == ".":
            s += "O"
        else:
            s += "X"; n += 1
        s += w[i][j % len(w[0]) + 1 :]
        j += 3; i += 1
    print(n)
