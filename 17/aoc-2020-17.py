from operator import itemgetter

def nest(f, expr, n):
    assert n >= 0
    if n == 0:
        return expr
    else:
        return f(nest(f, expr, n - 1))

with open('input.txt') as f:
    puzzle = [line.strip() for line in f.readlines()]

cubes = set()
for (y, value) in enumerate(puzzle):
    for (x, character) in enumerate(list(value)):
        if character == '#':
            cubes.add((x, y, 0))

def neighbors(x, y, z):
    r = [-1, 0, 1]
    for dx, dy, dz in ((dx, dy, dz) for dx in r for dy in r for dz in r):
        if not (dx == dy == dz == 0):
            yield (x + dx, y + dy, z + dz)

def count_neighbors(S, x, y, z):
    c = 0
    for xn, yn, zn in neighbors(x, y, z):
        if (xn, yn, zn) in S:
            c += 1
    return c

def cycle(S):
    R = set()
    T = set()
    for (x, y, z) in S:
        if count_neighbors(S, x, y, z) in [2, 3]:
            T.add((x, y, z))
        else:
            R.add((x, y, z))

        for (xn, yn, zn) in neighbors(x, y, z):
            if (xn, yn, zn) not in S and count_neighbors(S, xn, yn, zn) == 3:
                T.add((xn, yn, zn))
    return T.difference(R)

def print_layer(S, z):
    xl = min(S, key=itemgetter(0))[0]
    xr = max(S, key=itemgetter(0))[0]
    yl = min(S, key=itemgetter(1))[1]
    yr = max(S, key=itemgetter(1))[1]
    for y in range(yl, yr + 1):
        for x in range(xl, xr + 1):
            if (x, y, z) in S:
                print('#', end='')
            else:
                print('.', end='')
        print()

print('Part 1:', len(nest(cycle, cubes, 6)))

hypercubes = set()
for (y, value) in enumerate(puzzle):
    for (x, character) in enumerate(list(value)):
        if character == '#':
            hypercubes.add((x, y, 0, 0))

def hyperneighbors(x, y, z, w):
    r = [-1, 0, 1]
    for dx, dy, dz, dw in ((dx, dy, dz, dw) for dx in r for dy in r for dz in r for dw in r):
        if not (dx == dy == dz == dw == 0):
            yield (x + dx, y + dy, z + dz, w + dw)

def count_hyperneighbors(S, x, y, z, w):
    c = 0
    for xn, yn, zn, wn in hyperneighbors(x, y, z, w):
        if (xn, yn, zn, wn) in S:
            c += 1
    return c

def hypercycle(S):
    R = set()
    T = set()
    for (x, y, z, w) in S:
        if count_hyperneighbors(S, x, y, z, w) in [2, 3]:
            T.add((x, y, z, w))
        else:
            R.add((x, y, z, w))

        for (xn, yn, zn, wn) in hyperneighbors(x, y, z, w):
            if (xn, yn, zn, wn) not in S and count_hyperneighbors(S, xn, yn, zn, wn) == 3:
                T.add((xn, yn, zn, wn))
    return T.difference(R)

print('Part 2:', len(nest(hypercycle, hypercubes, 6)))