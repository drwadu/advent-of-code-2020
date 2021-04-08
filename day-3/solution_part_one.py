with open("input.txt", "r") as f:
    w = list(map(lambda s: s.replace("\n", ""), f.readlines()))
    l, x, y = len(w[0]), 3, 1
    n = 0 if not w[y][x] == "X" else 1
    while y < len(w):
        if w[y][x % l] == "#":
            n += 1;
        else: pass 
        x += 3; y += 1
    print(n)
