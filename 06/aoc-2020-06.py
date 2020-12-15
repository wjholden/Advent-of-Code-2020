with open("input.txt") as f:
    puzzle = f.read().strip().split('\n\n')

def yes_answers(puzzle, fcn):
    for group in puzzle:
        yield len(fcn(*(set(s) for s in group)))

puzzle = [line.split() for line in puzzle]

print("Part 1:", sum(yes_answers(puzzle, set.union)))

print("Part 2:", sum(yes_answers(puzzle, set.intersection)))
