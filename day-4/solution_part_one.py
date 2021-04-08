with open("input.txt", "r") as f:
    d = "".join(f.readlines()).split("\n\n")
    n = 0
    for i in d:
        if i.count(":") == 8 or (i.count(":") == 7 and "cid" not in i): 
            n += 1
    print(n)
