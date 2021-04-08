koits = None 
with open('input.txt', 'r') as f:
    inss = list(map(lambda s: s.replace('\n', ''), f.readlines()))
    d = {i: inss[i].split(' ') for i in range(len(inss))}
    koits = [i for i, j in d.items() if j[0] in ['nop', 'jmp']] 
    
for i in koits:
    ACC, l = 0, []
    
    def run(ins, n, g):
        global ACC, l 
        
        if n in l: return

        l.append(n)
        p = lambda e: -int(e[1:]) if e[0] == '-' else int(e[1:])
        i = ins[0]

        try:
            if i == 'acc': ACC += p(ins[1])
                run(g[n+1], n+1, g)
            elif i == 'jmp': by = p(ins[1])
                run(g[n+by], n+by, g)
            else: run(g[n+1], n+1, g)

        except: 
            print(ACC)
            quit() 
    d = None

    with open('input.txt', 'r') as f:
        inss = list(map(lambda s: s.replace('\n', ''), f.readlines()))
        d = {i: inss[i].split(' ') for i in range(len(inss))}

    if d[i][0] == 'jmp': d[i] = ['nop', d[i][1]]
    else: d[i] = ['jmp', d[i][1]]

    run(d[0], 0, d)
