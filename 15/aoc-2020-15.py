example = [0, 3, 6]
puzzle =  [2, 1, 10, 11, 0, 6]

def memory_game(numbers, limit):
    i = 0
    say = 0
    said = {}

    while i < limit:
        if i < len(numbers):
            say = numbers[i]
            said[say] = i + 1
        else:
            if say in said.keys():
                diff = i - said[say]
                said[say] = i
                say = diff
            else:
                said[say] = i
                say = 0
        i += 1
    return say

def memory_game2(numbers, limit):
    '''
    Influenced by https://www.reddit.com/r/adventofcode/comments/kdf85p/2020_day_15_solutions/gfxndm6?utm_source=share&utm_medium=web2x&context=3
    This is surprisingly much faster. I guess the extra comparison and third dict() lookup are not so cheap.
    '''
    said = {value: turn for (turn, value) in enumerate(numbers, 1)}
    say = numbers[-1]
    for i in range(len(numbers), limit):
        said[say], say = i, i - said.get(say, i)
    return say

print("Part 1:", memory_game(puzzle, 2020))
print("Part 1:", memory_game(puzzle, int(3e7)))