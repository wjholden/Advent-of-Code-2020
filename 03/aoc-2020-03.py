import os

def parse_input(format, filename):
    return [format(line) for line in open(filename).readlines()]

def formatter(line):
    return list(line.strip())

def count_trees(M, right, down):
    y = 0
    x = 0
    trees = 0
    while (y < len(M)):
        if (M[y][x] == '#'):
            trees += 1
        y += down
        x = (x + right) % len(M[0])
    return trees

M = parse_input(formatter, "input.txt")

print("Part 1", count_trees(M, 3, 1))

print("Part 2", count_trees(M, 1, 1) * count_trees(M, 3, 1) * count_trees(M, 5, 1) * count_trees(M, 7, 1) * count_trees(M, 1, 2))

M = parse_input(formatter, "test.txt")
print("Upping the ante", count_trees(M, 1, 3))
