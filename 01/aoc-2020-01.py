import os

def parse_input(filename):
    with open(filename) as f:
        content = f.readlines()
    return [int(x.strip()) for x in content]

a = sorted(parse_input("input.txt"))
for x in a:
    for y in a:
        if x + y == 2020:
            print("Part 1", x, y, x + y, x * y)

# This is also pretty neat.
print("Part 2", [(x, y, z, x + y + z, x * y * z) for x in a for y in a for z in a if x + y + z == 2020 and x <= y and y <= z])
