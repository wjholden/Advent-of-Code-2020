import re

def parse(filename):
    current = {}
    key_value_pairs = [current]
    with open(filename) as f:
        for line in f.readlines():
            # A better way to do this would have been to read all of the file at once,
            # then split inputs by \n\n. Then, the dict() constructor may be able to 
            # help with parsing key-value pairs as well.
            l = re.split(' |:', line.strip())
            if len(l) > 1:
                for i in range(0, len(l), 2):
                    current[l[i]] = l[i + 1]
            else:
                current = {}
                key_value_pairs.append(current)
    return key_value_pairs

def valid_passport(d):
    for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if not field in d:
            return False
    return True

def valid_height(hgt):
    units = hgt[-2:]
    qty = int(re.compile(r"\d+").match(hgt).group(0))

    if units == 'cm':
        return 150 <= qty <= 193
    elif units == 'in':
        return 59 <= qty <= 76
    return False

def valid_passport2(d):
    hcl_regexp = re.compile(r"^#[a-f0-9]{6}$")
    cid_regexp = re.compile(r"^\d{9}$")

    return all([1920 <= int(d['byr']) <= 2002,
        2010 <= int(d['iyr']) <= 2020,
        2020 <= int(d['eyr']) <= 2030,
        valid_height(d['hgt']),
        bool(re.match(hcl_regexp, d['hcl'])),
        d['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        bool(re.match(cid_regexp, d['pid']))]) # could also have used str.isdigit

FILE = 'input.txt'

print("Part 1:", sum(1 if valid_passport(d) else 0 for d in parse(FILE)))

print("Part 2:", sum(1 if valid_passport(d) and valid_passport2(d) else 0 for d in parse(FILE)))
