with open('input.txt', 'r') as f:
    inss = list(map(lambda s: s.replace('\n', ''), f.readlines()))
    d = {i: inss[i].split(' ') for i in range(len(inss))}
    
    ACC, l = 0, []

    def run(ins, n):
        global ACC, l
        
        if n in l:
            print(ACC)
            quit()

        l.append(n)
        p = lambda e: -int(e[1:]) if e[0] == '-' else int(e[1:])
        i = ins[0]
        if i == 'acc':
            ACC += p(ins[1])
            run(list(d.values())[n+1], n+1)
        elif i == 'jmp':
            by = p(ins[1])
            run(list(d.values())[n+by], n+by)
        else:
            run(list(d.values())[n+1], n+1)

    for n, ins in d.items():
        run(ins, n)

