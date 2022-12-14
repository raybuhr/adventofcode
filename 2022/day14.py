with open("input.txt") as f:
    lines = f.read().splitlines()


test_lines = ["498,4 -> 498,6 -> 496,6", "503,4 -> 502,4 -> 502,9 -> 494,9"]


def line_to_points(line):
    rocks = []
    points = [
        (int(x), -int(y)) for x, y in [line.split(",") for line in line.split(" -> ")]
    ]
    ax, ay = points.pop()
    while points:
        bx, by = points.pop()
        if ax > bx and ay == by:
            for x in range(bx, ax + 1):
                rocks.append((x, ay))
        if ax < bx and ay == by:
            for x in range(ax, bx + 1):
                rocks.append((x, ay))
        if ay > by and ax == bx:
            for y in range(by, ay + 1):
                rocks.append((ax, y))
        if ay < by and ax == bx:
            for y in range(ay, by + 1):
                rocks.append((ax, y))
        ax, ay = bx, by
    return rocks


def show_rocks(lines):
    rocks = set()
    for line in lines:
        points = line_to_points(line)
        for pt in points:
            rocks.add(pt)
    return rocks


def drop_sand(rocks, sand):
    x, y = 500, 0
    bottom = min(y for x, y in rocks)
    while True:
        if y <= bottom:
            return None
        if (x, y-1) not in rocks and (x, y-1) not in sand:
            y -= 1
            continue
        if (x-1, y-1) not in rocks and (x-1, y-1) not in sand:
            x -= 1
            y -= 1
            continue
        if (x+1, y-1) not in rocks and (x+1, y-1) not in sand:
            x += 1
            y -= 1
            continue
        break
    return x, y


def rain_sand(rocks):
    sand = set()
    x, y = None, None
    while True:
        position = drop_sand(rocks, sand)
        if not position:
            break
        sand.add(position)
        if position == (500, 0):
            break
    return sand


def add_floor(rocks):
    rocks_ = [r for r in rocks]
    y = min(y for x, y in rocks) - 2
    left = min(x for x, y in rocks) - abs(y)
    right = max(x for x, y in rocks) + abs(y)
    for x in range(left, right+1):
        rocks_.append((x, y))
    return set(rocks_)


def test():
    test_rocks = show_rocks(test_lines)
    test_sand = rain_sand(test_rocks)
    assert len(test_sand) == 24
    test_rocks = add_floor(test_rocks)
    test_sand = rain_sand(test_rocks)
    assert len(test_sand) == 93
    return True


def solve():
    rocks = show_rocks(lines)
    sand = rain_sand(rocks)
    print("part a:", len(sand))
    rocks = add_floor(rocks)
    sand = rain_sand(rocks)
    print("part b:", len(sand))

if __name__ == "__main__":
    solve()