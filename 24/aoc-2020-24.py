def build_path(line):
    path = []
    i = 0
    while i < len(line):
        c = line[i]
        if c == 'n' or c == 's':
            path.append(line[i:i + 2])
            i += 2
        else:
            path.append(c)
            i += 1
    return path

with open('input.txt') as f:
    puzzle = (build_path(line) for line in f.read().split())

def follow_path(path):
    x = 0
    y = 0
    moves = {
        'w':  (-2,  0),
        'e':  ( 2,  0),
        'sw': (-1, -1),
        'nw': (-1,  1),
        'se': ( 1, -1),
        'ne': ( 1,  1)
    }
    for tile in path:
        (dx, dy) = moves[tile]
        (x, y) = (x + dx, y + dy)
    return (x, y)

tiles = [follow_path(path) for path in puzzle]

from collections import Counter
counts = Counter(tiles)
assert set(counts.values()) == {1, 2}

print('Part 1:', list(counts.values()).count(1))

black_tiles = set()
# I don't like this, but I can't figure out how to get both (x, y)
# from the key with list comprehension.
for key, value in dict(counts).items():
    if value == 1:
        black_tiles.add(key)

# Memoization gives about 800ms of speedup on my machine.
from functools import cache
@cache
def neighbors(x, y):
    return set([(x + dx, y + dy) for (dx, dy) in [(-2, 0), (2, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]])

def flip(tiles):
    to_black = set()
    to_white = set()
    for (x, y) in tiles: # iterate over every black tile
        n = neighbors(x, y)
        black_neighbors = n.intersection(tiles)
        white_neighbors = n.difference(black_neighbors)
        if len(black_neighbors) == 0 or len(black_neighbors) > 2:
            to_white.add((x, y))
        for (wx, wy) in white_neighbors:
            # You would think that testing if (wx, wy) is already in
            # to_black would help, but in fact it makes no difference.
            wn = neighbors(wx, wy).intersection(tiles)
            if len(wn) == 2:
                to_black.add((wx, wy))
    return tiles.difference(to_white).union(to_black)

exhibits = [black_tiles]
for i in range(1, 101):
    e = exhibits[-1]
    exhibits.append(flip(e))
    #print(f'Day {i}: {len(exhibit[-1])}')

print('Part 2:', len(exhibits[-1]))

# upping the ante...messing around with sea monsters from day 20.
exit()

from operator import itemgetter
def print_exhibit(exhibit):
    xmin = min(exhibit, key=itemgetter(0))[0]
    xmax = max(exhibit, key=itemgetter(0))[0]
    ymin = min(exhibit, key=itemgetter(1))[1]
    ymax = max(exhibit, key=itemgetter(1))[1]
    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            if (x, y) in exhibit:
                print('#', end='')
            else:
                print(' ', end='')
        print()

def read_dragon():
    with open('dragon.txt') as d:
        dragon_lines = d.readlines()
    for y in range(len(dragon_lines)):
        line = list(dragon_lines[y])
        for x in range(len(line)):
            if line[x] == '#':
                yield (x, y)

dragons = [set(read_dragon())]
for i in range(1000):
    print_exhibit(dragons[-1])
    if dragons[0] <= dragons[i] and i > 0:
        print('Found a dragon in a dragon!')
    input('Press enter to continue...')
    dragons.append(flip(dragons[-1]))

