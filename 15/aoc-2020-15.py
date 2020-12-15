example = [0, 3, 6]
puzzle =  [2, 1, 10, 11, 0, 6]

def memory_game(numbers, limit):
    i = 0
    say = 0
    said = {}

    while i < limit:
        if i < len(numbers):
            say = numbers[i]
            said[say] = i
        else:
            if say in said.keys():
                diff = i - said[say] - 1
                said[say] = i - 1
                say = diff
            else:
                said[say] = i - 1
                say = 0
        i += 1
    return say
    
print("Part 1:", memory_game(puzzle, 2020))
print("Part 1:", memory_game(puzzle, 3e7))