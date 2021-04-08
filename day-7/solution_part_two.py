with open('input.txt', 'r') as f:
    d = list(map(lambda s: s.split('contain'), f.readlines()))

    def trace_bag(bag):
        x = 0
        for rule in d:
            if bag in rule[0]: 
                bs = [b[3:].replace('\n', '').replace('.', '').split('bag')[0].strip() 
                        for b in rule[1].split(',')]
                ms = [int(c) for c in rule[1].split() if c.isdigit()]
                if ms:
                    for b in bs:
                        m = ms[bs.index(b)]
                        x += m * trace_bag(b) 
                        x += m
        return x

    print(trace_bag('shiny gold'))
