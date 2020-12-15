import re
from operator import xor

def parse_line(line):
    return tuple(re.split('-| |: ', line.strip()))

def get_input(f):
    return [parse_line(line) for line in open(f).readlines()]

def valid_password(t):
    min, max, symbol, password = t
    c = password.count(symbol)
    return int(min) <= c <= int(max)

print("Part 1:", len(list(filter(valid_password, get_input("input.txt")))))

def valid_password2(t):
    start, end, symbol, password = t
    return xor(password[int(start) - 1] == symbol, password[int(end) - 1] == symbol)

print("Part 2:", len(list(filter(valid_password2, get_input("input.txt")))))