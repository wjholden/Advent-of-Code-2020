import numpy as np

def t(x, y):
    return np.array([(1, 0, x), (0, 1, y), (0, 0, 1)])

r ={
        90: np.array([(0, -1, 0), (1, 0, 0), (0, 0, 1)]),
        180: np.array([(-1, 0, 0), (0, -1, 0), (0, 0, 1)]),
        270: np.array([(0, 1, 0), (-1, 0, 0), (0, 0, 1)])
    }

with open('input.txt') as f:
    input = [(line[0:1], int(line[1:])) for line in f.readlines()]

m = r[270] # start with a vector pointing east
v = np.array([0, 0, 1])

for (inst, amount) in input:
    # left is global, right is local
    if inst == 'N':
        m = t(0, amount) @ m
    elif inst == 'S':
        m = t(0, -amount) @ m
    elif inst == 'E':
        m = t(amount, 0) @ m
    elif inst == 'W':
        m = t(-amount, 0) @ m
    elif inst == 'L':
        m = m @ r[amount]
    elif inst == 'R':
        m = m @ r[360 - amount]
    elif inst == 'F':
        m = m @ t(0, amount)
    else:
        raise Exception(inst, amount)
    #print(m @ v, inst, amount)

x, y, z = tuple(m @ v)
print("Part 1:", abs(x) + abs(y))

wp = t(10, 1)
p = np.array([0, 0, 1])
for (inst, amount) in input:
    if inst == 'N':
        wp = t(0, amount) @ wp
    elif inst == 'S':
        wp = t(0, -amount) @ wp
    elif inst == 'E':
        wp = t(amount, 0) @ wp
    elif inst == 'W':
        wp = t(-amount, 0) @ wp
    elif inst == 'L':
        wp = r[amount] @ wp
    elif inst == 'R':
        wp = r[360 - amount] @ wp
    elif inst == 'F':
        p = p + (wp @ np.array([0, 0, 1])) * amount
    else:
        raise Exception(inst, amount)
    #print(wp, p, inst, amount)

x, y, z = tuple(p)
print("Part 2:", abs(x) + abs(y))