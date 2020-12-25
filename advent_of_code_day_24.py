import os

os.chdir("Text input")

def move(coords, d):
    x, y, z = coords
    assert x + y + z == 0 and d in ["e", "w", "se", "sw", "ne", "nw"]
    if d == "e":
        return (x + 1, y - 1, z)
    if d == "w":
        return (x - 1, y + 1, z)
    if d == "ne":
        return (x + 1, y, z - 1)
    if d == "nw":
        return (x, y + 1, z - 1)
    if d == "se":
        return (x, y - 1, z + 1)
    if d == "sw":
        return (x - 1, y, z + 1)


def parse_line(l):
    steps = []
    l = list(l.strip())
    while len(l) > 0:
        c = l.pop(0)
        if c not in 'we':
            c += l.pop(0)
        steps.append(c)
    return steps
    

def get_neighbors(coords):
    return [move(coords, d) for d in ["e", "w", "se", "sw", "ne", "nw"]]


# part 1

tiles_are_flipped = dict()

INPUT_FILE = "lobby_layout.txt"

for line in open(INPUT_FILE):
    steps = parse_line(line)
    coord = (0,0,0)
    for step in steps:
        coord = move(coord, step)
    is_flipped = tiles_are_flipped.get(coord, False)
    tiles_are_flipped[coord] = not is_flipped

print(sum(v for v in tiles_are_flipped.values() if v))
