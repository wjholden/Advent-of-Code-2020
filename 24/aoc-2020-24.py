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
# I don't like this, but I can't figure out how to get both (x,y)
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
    # iterate over every black tile
    for (x, y) in tiles:
        n = neighbors(x, y)
        black_neighbors = n.intersection(tiles)
        white_neighbors = n.difference(black_neighbors)
        if len(black_neighbors) == 0 or len(black_neighbors) > 2:
            to_white.add((x, y))
        for (wx, wy) in white_neighbors:
            # You would think that a condition here to test if (wx, wy) is already
            # in to_black would help, but in fact it makes no difference.
            wn = neighbors(wx, wy).intersection(tiles)
            if len(wn) == 2:
                to_black.add((wx, wy))
    return tiles.difference(to_white).union(to_black)

exhibit = [black_tiles]
for i in range(1, 101):
    e = exhibit[-1]
    exhibit.append(flip(e))
    #print(f'Day {i}: {len(exhibit[-1])}')

print('Part 2:', len(exhibit[-1]))
