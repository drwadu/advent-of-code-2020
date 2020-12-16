with open('input.txt', 'r') as f:
    d, s = [], '' 
    for l in f.readlines():
        if l == '\n': 
            if s: d += [len(set(s))]
            s = ''
            continue
        else: 
            s += l.replace('\n', '')

    print(sum(d))
