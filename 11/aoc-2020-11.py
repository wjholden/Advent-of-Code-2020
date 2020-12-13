import copy
import cProfile
from math import inf
from collections import defaultdict
import numpy as np

with open('example.txt') as f:
    input = [list(line.strip()) for line in f.readlines()]

def neighbor_counts2(m):
    rows = len(m)
    cols = len(m[0])
    counts = [[0 for j in range(cols)] for i in range(rows)]
    adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for row in range(rows):
        for col in range(cols):
            if m[row][col] == '#':
                for (i, j) in adj:
                    if (0 <= i + row < rows) and (0 <= j + col < cols):
                        counts[row + i][col + j] += 1
    return counts

def seat_shuffle3(m):
    c = neighbor_counts2(m)
    change = False
    for (row, col) in ((row, col) for row in range(len(m)) for col in range(len(m[0]))):
        if m[row][col] == '#' and c[row][col] >= 4:
            m[row][col] = 'L'
            change = True
        elif m[row][col] == 'L' and c[row][col] == 0:
            m[row][col] = '#'
            change = True
    return m, change

def part1_mutable(input):
    m = copy.deepcopy(input)
    change = True
    while change:
        m, change = seat_shuffle3(m)
    return sum((row.count('#') for row in m))

#print("Part 1:", part1_mutable(input))
#cProfile.run('part1_mutable(input)')

def seats_to_vec(input):
    seats = set()
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == 'L':
                seats.add((x, y, False))
    return seats

def distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def angle(x1, y1, x2, y2):
    return (np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi) % 360

def neighbor_count_vec(x1, y1, seats):
    init = (inf, False)
    d = { 0: init, 45: init, 90: init, 135: init, 180: init,
        225: init, 270: init, 315: init }
    for (x2, y2, occupied) in seats:
        if x1 == x2 and y1 == y2:
            continue
        md = distance(x1, y1, x2, y2)
        a = angle(x1, y1, x2, y2)
        if a in d.keys() and md < d[a][0]:
            d[a] = (md, occupied)
    return sum([int(v[1]) for v in d.values()])

def seat_shuffle_vec(seats):
    s2 = set()
    for (x, y, occupied) in seats:
        neighbors = neighbor_count_vec(x, y, seats)
        if occupied and neighbors >= 5:
            s2.add((x, y, False))
        elif not occupied and neighbors == 0:
            s2.add((x, y, True))
        else:
            s2.add((x, y, occupied))
    return s2

def part2(input):
    seats = seats_to_vec(input)
    prev = None
    while seats != prev:
        prev = seats
        seats = seat_shuffle_vec(seats)
    return sum([int(s[2]) for s in seats])

print("Part 2:", part2(input))
cProfile.run('part2(input)')