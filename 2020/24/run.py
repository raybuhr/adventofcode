from aocd import get_data
from collections import defaultdict


MOVES = {
    "e": (2, 0),
    "w": (-2, 0),
    "se": (1, -1),
    "sw": (-1, -1),
    "nw": (-1, 1),
    "ne": (1, 1),
}


def parse_directions(directions):
    steps_list = list(directions)
    steps = []
    while steps_list:
        step = steps_list.pop(0)
        if step not in MOVES:
            step += steps_list.pop(0)
        steps.append(step)
    return steps


def identify_tile(steps):
    at = [0, 0]
    for step in steps:
        x, y = MOVES[step]
        at[0] += x
        at[1] += y
    return tuple(at)


def flip_tile(x, y, color, tiles):
    neighbors = [(x + x_i, y + y_i) for x_i, y_i in MOVES.values()]
    neighbor_colors = [tiles[n] for n in neighbors]
    num_black = sum(neighbor_colors)
    if color == 1:
        return 0 if num_black not in (1, 2) else 1
    if color == 0:
        return 1 if num_black == 2 else 0


def solve_part_a(data):
    seen = defaultdict(int)
    for d in data.splitlines():
        seen[identify_tile(parse_directions(d))] += 1
    return sum(v % 2 for v in seen.values())


def solve_part_b(data, days=100):
    tiles = defaultdict(int)
    day = 0
    for d in data.splitlines():
        tiles[identify_tile(parse_directions(d))] += 1
    for k, v in tiles.items():
        tiles[k] = v % 2
    while day < days:
        day += 1
        # add adjacent tiles
        flip = {k: v for k, v in tiles.items()}
        for tile, color in flip.items():
            x, y = tile
            neighbors = [(x + x_i, y + y_i) for x_i, y_i in MOVES.values()]
            neighbor_colors = [tiles[n] for n in neighbors]
        # figure out what to flip
        flip = {k: v for k, v in tiles.items()}
        for tile, color in flip.items():
            x, y = tile
            flip[tile] = flip_tile(x, y, color, tiles)
        for tile, color in flip.items():
            tiles[tile] = color
    return sum(tiles.values())


if __name__ == "__main__":
    data = get_data(year=2020, day=24)
    print("Part 1:")
    a = solve_part_a(data)
    print(a)

    print("Part 2:")
    b = solve_part_b(data)
    print(b)
