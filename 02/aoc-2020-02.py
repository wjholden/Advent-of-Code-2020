import re
from operator import xor

def parse_line(line):
    return tuple(re.split('-| |: ', line.strip()))

def get_input(file):
    return [parse_line(line) for line in open(file).readlines()]

def valid_password(tuple):
    min, max, symbol, password = tuple
    c = password.count(symbol)
    return int(min) <= c <= int(max)

print("Part 1:", len(list(filter(valid_password, get_input("input.txt")))))

def valid_password2(tuple):
    start, end, symbol, password = tuple
    return xor(password[int(start) - 1] == symbol, password[int(end) - 1] == symbol)

print("Part 2:", len(list(filter(valid_password2, get_input("input.txt")))))