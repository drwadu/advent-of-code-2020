with open("input.txt", "r") as f:
    w = list(map(lambda s: s.replace("\n", ""), f.readlines()))
    l = len(w[0]); m = 1; 
    for i, j in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
        n = 0 if not w[i][j] == "X" else 1
        x = j; y = i;
        while y < len(w):
            if w[y][x % l] == "#":
                n += 1;
            else: pass 
            x += j; y += i
        m *= n
    print(m)
