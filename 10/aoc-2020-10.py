from functools import cache

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

@cache
def count_paths(joltage):
    # I would prefer a pure function, but @lru_cache doesn't want to memoize a set() object.
    global input
    if joltage == 0:
        return 1
    elif not joltage in input:
        return 0
    else:
        return sum([count_paths(joltage - i) for i in [1, 2, 3]])

lo, hi = count_adapter_differences(0, input)
print("Part 1:", lo * hi)

print("Part 2:", count_paths(max(input)))