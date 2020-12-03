# run 'pip install z3-solver' to install this
from z3 import *
import os
import time

INPUT_FILE = "test.txt"

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

def no_tree_indices(matrix):
    p = []
    for row in matrix:
        a = []
        for i in range(0, len(row)):
            if row[i] == '.':
                a.append(i)
        p.append(a)
    return p

def constraints_for_safe_path(safe_positions, dy):
    # instantiate a new Z3 solver
    s = Solver()

    dx = Int('dx')
    s.add(dx > 0)

    y = Int('dy')
    s.add(y == dy)

    for i in range(0, len(safe_positions), dy):
        # for each row, there should be some value dx such that 
        row = safe_positions[i]
        # Is this Or safe? Might need to turn this into some kind of Exactly-One-Of constraint.
        # (Note: Xor is not the solution. T xor T xor T == T. It does not work as a one-of gate.)
        constraint = Or([ (dx * i) % (width) == p for p in row ])
        #print(constraint)
        s.add(constraint)
    return dx, s

input_matrix = parse_input(formatter, INPUT_FILE)
width = len(input_matrix[0])
depth = len(input_matrix)
safe_positions = no_tree_indices(input_matrix)
#print("safe positions", safe_positions)

# Set a random seed to get a variety of results from Z3.
set_param("smt.random_seed", int(time.time()))

for dy in range(1, depth):
    dx, s = constraints_for_safe_path(safe_positions, dy)
    satisfiable = s.check()
    if satisfiable == sat:
        # if count_trees finds a nonzero number of trees then this is a spurious (false positive) solution.
        print(dy, satisfiable, s.model(), count_trees(input_matrix, s.model()[dx].as_long(), dy))
    else:
        print(dy, satisfiable)
