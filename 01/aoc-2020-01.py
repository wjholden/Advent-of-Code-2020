def parse_input(filename):
    with open(filename) as f:
        content = f.readlines()
    return [int(x.strip()) for x in content]

def part1(a):
    for x in a:
        for y in a:
            if x + y == 2020:
                return (x, y, x + y, x * y)

# This is also pretty neat.
#print("Part 2", [(x, y, z, x + y + z, x * y * z) for x in a for y in a for z in a if x + y + z == 2020 and x <= y and y <= z])

def part2(a):
    # iterate over generator expression so that we can return early as soon as we find a solution.
    for solution in ((x, y, z, x + y + z, x * y * z) for x in a for y in a for z in a if x + y + z == 2020 and x <= y and y <= z):
        return solution

a = sorted(parse_input("input.txt"))

print("Part 1:", part1(a))

print("Part 2:", part2(a))
