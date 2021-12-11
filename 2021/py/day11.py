import sys


def make_grid(filename):
    with open(filename) as file:
        data = file.read()
    return [[int(n) for n in line] for line in data.splitlines()]


def find_neighbors(grid, x, y):
    neighbors = []
    for direction in [
        (1, 0),
        (1, -1),
        (1, 1),
        (0, 1),
        (0, -1),
        (-1, 0),
        (-1, 1),
        (-1, -1),
    ]:
        try:
            nx, ny = direction[0] + x, direction[1] + y
            if (
                nx >= 0
                and ny >= 0
                and nx < len(grid[0])
                and ny < len(grid)
                and (nx, ny) not in neighbors
                and (nx, ny) != (x, y)
            ):
                neighbors += [(nx, ny)]
        except:
            continue
    return neighbors


def step(grid):
    rows = len(grid)
    grid = [[n + 1 for n in line] for line in grid]

    def get_flashes(grid):
        return [(x, y) for y in range(rows) for x in range(rows) if grid[y][x] > 9]

    flashed = []
    while True:
        flashes = [f for f in get_flashes(grid) if f not in flashed]
        if not flashes:
            break
        else:
            flash = flashes[0]
        flashed.append(flash)
        x, y = flash
        neighbors = find_neighbors(grid, x, y)
        for nb in neighbors:
            if nb not in flashes:
                grid[nb[1]][nb[0]] += 1

    for y in range(rows):
        for x in range(rows):
            if grid[y][x] > 9:
                grid[y][x] = 0
    return grid


def part_one(grid):
    ct = 0
    for _ in range(100):
        grid = step(grid)
        ct += sum(1 for row in grid for n in row if n == 0)
    return ct


def part_two(grid):
    ct = 100
    i = 0
    while ct:
        i += 1
        grid = step(grid)
        ct = sum(n for row in grid for n in row)
    return i


if __name__ == "__main__":
    filename = sys.argv[1]
    data = make_grid(filename)
    print("Part One")
    print(part_one(data))
    print("Part Two")
    print(part_two(data))
