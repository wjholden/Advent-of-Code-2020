# run 'pip install z3-solver' to install this
from z3 import *
import os

INPUT_FILE = "test.txt"

def parse_input(format, filename):
    return [format(line) for line in open(filename).readlines()]

def formatter(line):
    return list(line.strip())

def no_tree_indices(matrix):
    p = []
    for row in matrix:
        a = []
        for i in range(0, len(row)):
            if row[i] == '.':
                a.append(i)
        p.append(a)
    return p

# This test case is trivially satisfiable with dx = 1.
# Start at 0,0, then go to 1,1, then to 2,2.
#input_matrix = [['.', '#', '.'], ['#', '.', '#'], ['#', '#', '.']]

# Apparently this small test case is impossible.
#input_matrix = [['#', '#', '.'], ['#', '.', '#'], ['#', '#', '.']]

input_matrix = parse_input(formatter, INPUT_FILE)
width = len(input_matrix[0])
depth = len(input_matrix)
safe_positions = no_tree_indices(input_matrix)
print("safe positions", safe_positions)

# instantiate a new Z3 solver
s = Solver()

# The amount we translate to the right on each turn.
dx = Int('dx')
s.add(dx > 0)
# For this experiment I want to keep dy = 1. Otherwise, we should get some uninteresting
# solutions where the machine just skips over all rows and declares victory.

i = 0
for row in safe_positions:
    # for each row, there should be some value dx such that 
    constraint = Or([ (dx * i) % (width) == p for p in row ])
    print(constraint)
    s.add(constraint)
    i += 1

satisfiable = s.check()
print(satisfiable)
if satisfiable == sat:
    print(s.model()[dx])
