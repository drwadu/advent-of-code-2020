with open('input.txt', 'r') as f:
    d, s, n = [], '', 0 
    for l in f.readlines():
        if l == '\n': 
            if s: d += [len(list(set(filter(lambda c: s.count(c) == n, s))))]
            s, n = '', 0
            continue
        else: 
            s += l.replace('\n', '')
            n += 1
    
    print(sum(d))

