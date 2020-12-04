with open('input.txt', 'r') as f: 
    data, parse = f.readlines(), lambda d, c, i: d.replace('\n', '').replace(' ', '').split(c)[i]
    parsed_data = {
        i: 
            (
                parse(data[i], ':', 1),
                parse(data[i], ':', 0)[-1], 
                int(parse(parse(data[i], ':', 0), '-', 0)), 
                int(parse(parse(data[i], ':', 0), '-', -1)[:-1])
            ) for i in range(len(data))}
    is_valid = lambda p, mini, maxi, c: 1 if mini <= p.count(c) <= maxi else 0
    print(sum([is_valid(v[0], v[2], v[3], v[1]) for v in parsed_data.values()]))