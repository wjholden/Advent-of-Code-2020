from functools import lru_cache

with open('input.txt') as f:
    input = set([int(line) for line in f.readlines()])

def count_adapter_differences(joltage, s):
    if joltage + 1 in s:
        lo, hi = count_adapter_differences(joltage + 1, s)
        return lo + 1, hi
    elif joltage + 3 in s:
        lo, hi = count_adapter_differences(joltage + 3, s)
        return lo, hi + 1
    else:
        return 0, 1

@lru_cache
def count_paths(joltage, goal):
    # I would prefer a pure function, but @lru_cache doesn't want to memoize a set() object.
    global input
    if joltage == goal:
        return 1
    elif not joltage in input and joltage > 0:
        return 0
    else:
        return sum([count_paths(joltage + i, goal) for i in [1, 2, 3]])

lo, hi = count_adapter_differences(0, input)
print("Part 1:", lo * hi)

print("Part 2:", count_paths(0, 3 + max(input)))