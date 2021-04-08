with open("input.txt", "r") as f:
    d, n = "".join(f.readlines()).split("\n\n"), 0
    for i in d:
        if i.count(":") == 8 or (i.count(":") == 7 and "cid" not in i):
            s = sorted(i.replace("\n", " ").split(" "))
            for j in s:
                if "cid" in j:
                    s.remove(j)
            dd = {s.index(i): i.split(":")[1] for i in s}
            if (
                sum(
                    map(
                        int,
                        [
                            len(dd[0]) == 4 and 1920 <= int(dd[0]) <= 2002,
                            dd[1] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                            len(dd[2]) == 4 and 2020 <= int(dd[2]) <= 2030,
                            dd[3][0] == "#"
                            and all(
                                filter(
                                    lambda c: c.isdigit() or 102 <= ord(c) <= 102,
                                    dd[4][0:],
                                )
                            ),
                            dd[4][-2:] in ["cm", "in"]
                            and (
                                150 <= int(dd[4][:-2]) <= 193
                                if dd[4][-2:] == "cm"
                                else 59 <= int(dd[4][:-2]) <= 76
                            ),
                            len(dd[5]) == 4 and 2010 <= int(dd[5]) <= 2020,
                            len(dd[6]) == 9
                            and all(filter(lambda c: c.isdigit(), dd[6])),
                        ],
                    )
                )
                == 7
            ):
                n += 1
    print(n)
