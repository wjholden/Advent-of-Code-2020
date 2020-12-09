with open('input.txt') as f:
    input = [int(line) for line in f]

def is_valid(a, i, preamble_length):
    s = a[i]
    addends = a[i - preamble_length:i]
    pairs = ((x, y) for x in addends for y in addends if x != y)
    for (x,y) in pairs:
        if s == x + y:
            return True, s
    return False, s

def part1(a, preamble_length):
    for i in range(preamble_length, len(input)):
        valid, value = is_valid(input, i, preamble_length)
        if not valid:
            return value
            
value = part1(input, 25)
print("Part 1:", value)

# This program is a sliding window. 
left = 0
right = 0
total = 0
while total != value:
    if total < value:
        right += 1
    elif total > value:
        left += 1
    total = sum(input[left:right])
print("Part 2: ", min(input[left:right]) + max(input[left:right]))