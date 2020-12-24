import regex

with open('input.txt') as f:
    puzzle = f.readlines()

def part1(puzzle):
    mask = ''
    set_mask = 0
    clear_mask = 0
    mem = {}

    for line in puzzle:
        if line.startswith('mask'):
            mask = line.split()[2]
            setter = mask.replace('X', '0')
            clearer = mask.replace('X', '1')
            set_mask = int(setter, 2)
            clear_mask = int(clearer, 2)
        elif line.startswith('mem'):
            pattern = r"^mem\[(?P<address>\d+)\] = (?P<value>\d+)$"
            match = regex.match(pattern, line)
            address = int(match.group('address'))
            value = int(match.group('value'))
            #print('value:  ', format(value, '#036b'), ' (decimal ', value, ')', sep='')
            #print('mask:  ', mask)
            value |= set_mask
            value &= clear_mask
            #print('result: ', format(value, '#036b'), ' (decimal ', value, ')', sep='')
            mem[address] = value
        else:
            raise Exception('Unrecognized instruction: ' + line)
    return sum(mem.values())

def get_masks(m):
    if 'X' in m:
        x = m.index('X')
        for child in get_masks(m[x + 1:]):
            yield m[:x] + '1' + child
            yield m[:x] + '0' + child
    else:
        yield m

def part2(puzzle):
    mem = {}
    set_bits = 0
    masks = []
    for line in puzzle:
        if line.startswith('mask'):
            m = line.split()[2]
            set_bits = int(m.replace('X', '0'), 2)
            float_bits = m.replace('1', '0')
            masks = [int(mask, 2) for mask in get_masks(float_bits)]
        elif line.startswith('mem'):
            pattern = r"^mem\[(?P<address>\d+)\] = (?P<value>\d+)$"
            match = regex.match(pattern, line)
            address = int(match.group('address'))
            value = int(match.group('value'))
            for mask in masks:
                addr = (address | set_bits) ^ mask # tricky...
                mem[addr] = value
                #print(format(addr, '#036b'), ' (decimal ', addr, ')', sep='')
        else:
            raise Exception('Unrecognized instruction: ' + line)
    return sum(mem.values())


print('Part 1:', part1(puzzle))
print('Part 2:', part2(puzzle))
# 4313842651168 too high
# 4313446951814 too high