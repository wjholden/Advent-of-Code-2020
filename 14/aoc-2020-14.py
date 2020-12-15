import re

with open('example.txt') as f:
    puzzle = [line.strip() for line in f.readlines()]

print(puzzle)
values = {}

def mask_to_int(m):
    setb, clearb = 0, 0
    bits = list(m)
    print(m)
    for i in range(len(bits)):
        print(bits[i], bin(setb), bin(clearb))
        if bits[i] == '0':
            clearb = clearb | (1 << i)
        elif bits[i] == '1':
            setb = setb | (1 << i)
    return bin(setb), bin(clearb)

for line in puzzle:
    if line.startswith('mem'):
        p = re.compile(r'mem\[(?P<address>\d+)\] = (?P<value>\d+)')
        m = p.search(line)
        address = int(m.group('address'))
        value = int(m.group('value'))
        print(address)
        print(value)
    elif line.startswith('mask'):
        p = re.compile(r'mask = (?P<mask>[\dX]+)')
        m = p.search(line)
        mask = m.group('mask')
        print(mask, mask_to_int(mask))