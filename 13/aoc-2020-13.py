# pip install modint
from modint import chinese_remainder
from functools import reduce

with open('input.txt') as f:
    time = int(f.readline())
    l2 = f.readline().split(',')
    buses = [int(i) for i in (line for line in l2 if line != 'x')]
    
next_times = [(id, id - (time % id)) for id in buses]
next_bus = min(next_times, key = lambda t: t[1])

print("Part 1:", next_bus[0] * next_bus[1])

with open('input.txt') as f:
    ignore = f.readline()
    for line in f.readlines():
        ids = line.split(',')
        offsets = [(offset, int(id)) for (offset, id) in zip(range(len(ids)), ids) if id != 'x']
        #print(offsets)
        mods = [o[0] for o in offsets]
        n = [o[1] for o in offsets]
        prod = reduce(lambda x, y: x * y, n, 1)
        # Look, I enjoy math but I really never wrapped my head around modular arithmetic.
        # I also used to be above using library functions...not anymore.
        print("Part 2:", prod - chinese_remainder(n, mods))
