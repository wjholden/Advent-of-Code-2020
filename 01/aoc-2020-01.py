def parse_input(filename):
    with open(filename) as f:
        content = f.readlines()
    return [int(x.strip()) for x in content]

a = sorted(parse_input("input.txt"))
for x in a:
    for y in a:
        if x + y == 2020:
            print(x, y, x + y, x * y)

for x in a:
    for y in a:
        for z in a:
            if x + y + z == 2020:
                print(x, y, z, x + y + z, x * y * z)

# This is marginally faster than the above.
for x in a:
    for y in (y for y in a if x + y < 2020):
        for z in (z for z in a if x + y + z == 2020):
            print(x, y, z, x + y + z, x * y * z)

# This is also pretty neat.
[(x, y, z, x + y + z, x * y * z) for x in a for y in a for z in a if x + y + z == 2020 and x <= y and y <= z]