import sys


def parse_data(filename):
    with open(filename) as file:
        lines = file.read().splitlines()
    return [[int(n) for n in line] for line in lines]


def find_neighbors(data, x, y):
    neighbors = []
    if x > 0:
        col, row = x - 1, y
        if data[row][col] < 9:
            neighbors += [(col, row)]
    if x < len(data[0]) - 1:
        col, row = x + 1, y
        if data[row][col] < 9:
            neighbors += [(col, row)]
    if y > 0:
        col, row = x, y - 1
        if data[row][col] < 9:
            neighbors += [(col, row)]
    if y < len(data) - 1:
        col, row = (x, y + 1)
        if data[row][col] < 9:
            neighbors += [(col, row)]
    return neighbors


def part_one(data):
    lows = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            height = data[y][x]
            if height == 9:
                continue
            neighbors = find_neighbors(data, x, y)
            if all(data[ny][nx] > height for nx, ny in neighbors):
                lows.append(1 + height)
    return sum(lows)


def find_points_in_basin(data, x, y):
    if data[y][x] == 9:
        return 0
    points = [(x, y)]
    while True:
        length = len(points)
        for x, y in points:
            neighbors = find_neighbors(data, x, y)
            for nb in neighbors:
                if nb not in points:
                    points.append(nb)
        if len(points) == length:
            break
    return points


def part_two(data):
    basins = {}
    basins[0] = find_points_in_basin(data, 0, 0)
    b = 1
    for y in range(len(data)):
        for x in range(len(data[0])):
            seen = False
            for pts in basins.values():
                if (x, y) in pts:
                    seen = True
            if seen:
                continue
            if data[y][x] == 9:
                continue
            basins[b] = find_points_in_basin(data, x, y)
            b += 1
    three_largest = sorted([len(pts) for pts in basins.values()])[-3:]
    return three_largest[0] * three_largest[1] * three_largest[2]


if __name__ == "__main__":
    filename = sys.argv[1]
    data = parse_data(filename)
    print("Part One")
    print(part_one(data))
    print("Part Two")
    print(part_two(data))
