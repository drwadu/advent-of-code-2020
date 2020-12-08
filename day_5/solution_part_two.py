with open("input.txt", "r") as f:
    d = list(map(lambda s: s.replace("\n", ""), f.readlines()))
    r = lambda l, c: l[:len(l)//2] if c == "F" else l[len(l)//2+1:]
    c = lambda l, c: l[:len(l)//2] if c == "L" else l[len(l)//2+1:]
    def f(s):
        n, m = range(127), range(7)
        for ch in s[:7]: n = r(n, ch) 
        for ch in s[-3:]: m = c(m, ch)
        assert n.start == n.stop
        assert m.start == m.stop
        return n.start*8+m.start
    l = sorted(list(map(f, d)))
    for i in l:
        if not l[l.index(i+1)] == i+1:
            pass



