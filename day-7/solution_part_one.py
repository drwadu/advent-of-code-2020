with open('input.txt', 'r') as f:
    d, bs = list(map(lambda s: s.split('contain'), f.readlines())), []
    def trace_bag(bag):
        n = 0
        for rule in d:
            if bag in rule[1]: 
                b = rule[0][:-2] 
                bs.append(b)
                trace_bag(b)
        return len(set(bs)) 
    print(trace_bag('shiny gold'))

