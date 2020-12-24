from functools import reduce

def read_input(filename):
    with open(filename) as f:
        for tile in f.read().strip().split('\n\n'):
            a = tile.split('\n')
            tile_id = int(a[0].split(' ')[1][:-1])
            t = [list(row.strip()) for row in a[1:]]
            yield (tile_id, t)

def get_borders(tile):
    yield ''.join(tile[0]) # top
    yield ''.join(tile[-1]) # bottom 
    yield ''.join([row[0] for row in tile]) # left
    yield ''.join([row[-1] for row in tile]) # right

puzzle = read_input('input.txt')
borders = dict() # tile_id -> border
border_counts = dict() # border -> count
for tile_id, tile in puzzle:
    assert tile_id not in borders.keys()
    borders[tile_id] = set()
    for border in get_borders(tile):
        for border in [border, border[::-1]]:
            borders[tile_id].add(border)
            border_counts[border] = border_counts.get(border, 0) + 1

for b in borders.values():
    assert len(b) == 8 # verify an assumption that each tile has no duplicated borders

tile_weight = [(tile_id, sum([border_counts[b] for b in borders[tile_id]])) for tile_id in borders.keys()]
#print(tile_weight)
corners = [tile_id for (tile_id, weight) in tile_weight if weight == 12]
#print(corners)
print('Part 1:', reduce(lambda a, x: a * x, corners, 1))

#print(len(borders))
