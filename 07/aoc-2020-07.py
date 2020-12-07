import regex

def read_input(filename):
    pattern = r"^(?P<outer>[\w ]+) bags contain( no other bags)?( (?P<qty>\d) (?P<inner>[\w ]+) bag[s]?[,]?)*\.$"
    with open(filename) as f:
        for line in f.readlines():
            m = regex.search(pattern, line)
            outer = m.group('outer')
            yield outer
            for qty, inner in zip(m.captures('qty'), m.captures('inner')):
                yield outer, int(qty), inner

def get_edges(generator):
    d = dict()
    for x in generator:
        if type(x) == str:
            if not x in d:
                d[x] = []
        elif type(x) == tuple:
            d[x[0]].append((x[1], x[2]))
        else:
            raise ValueError('incorrect type from read_input')
    return d

def children(e, u):
    for (count, color) in e[u]:
        yield color
        for inside_color in children(e, color):
            yield inside_color

def invert(e):
    d = dict()
    for u, v in e.items():
        if not u in d:
            d[u] = []
        for (count, inner) in v:
            if not inner in d:
                d[inner] = []
            d[inner].append((count, u))
    #print(d)
    return d
    
e = get_edges(read_input('input.txt'))

print("Part 1", len(set(children(invert(e), 'shiny gold'))))

def contents(e, u):
    total = 0
    for (count, v) in e[u]:
        total += count + count * contents(e, v)
    return total

print("Part 2", contents(e, 'shiny gold'))