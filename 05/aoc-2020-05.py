def seat_id(s):
    return int(s.replace("F", "0").replace("B", "1").replace("L", "0").replace("R", "1"), 2)

with open("input.txt") as f:
    seats = [seat_id(line.strip()) for line in f.readlines()]
seats = sorted(seats)

print("Part 1", max(seats))

for i in range(1, len(seats) - 1): # skip edge cases
    if seats[i] + 1 != seats[i + 1]:
        print("Part 2", seats[i] + 1)
