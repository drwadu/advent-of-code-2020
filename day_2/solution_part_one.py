with open('input.txt', 'r') as f: 
    p = lambda d, c, i: d.replace('\n', '').replace(' ', '').split(c)[i]
    print(sum(map(lambda d: 1 if int(p(p(d, ':', 0), '-', 0)) <= p(d, ':', 1).count(p(d, ':', 0)[-1]) <= int(p(p(d, ':', 0), '-', -1)[:-1]) else 0, f.readlines())))