with open("example.txt") as f:
    input = f.read().strip().split('\n\n')

input = [line.split('\n') for line in input]

