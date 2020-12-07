import re

def read_input(filename):
    #s = r"^([\w ]+) bags contain (no other bags)?((\d) ([\w ]+) bag.+)*\.$"
    s = r"^([\w ]+) bags contain (no other bags|.+)\.$"
    print(s)
    pattern = re.compile(s)
    with open(filename) as f:
        for line in f.readlines():
            m = re.findall(pattern, line)
            yield m

for g in read_input("example.txt"):
    print(g)