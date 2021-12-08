from collections import defaultdict
import sys


def parse_data(filename):
    with open(filename) as file:
        lines = file.readlines()

    points = [line.replace(" -> ", ",").split(",") for line in lines]

    points = [[int(n) for n in line] for line in points]
    return points


def find_points_between(x1, y1, x2, y2, include_diagonal=False):
    points = []
    if x1 == x2:
        if y1 > y2:
            rng = range(y2, y1 + 1)
        if y2 > y1:
            rng = range(y1, y2 + 1)
        points += [(x1, r) for r in rng]
    if y1 == y2:
        if x1 > x2:
            rng = range(x2, x1 + 1)
        if x2 > x1:
            rng = range(x1, x2 + 1)
        points += [(r, y1) for r in rng]

    if include_diagonal:
        x, y = x1 - x2, y1 - y2
        if abs(x) == abs(y):
            slope = 1 if x * y > 0 else -1
            intercept = y1 - slope * x1
            if x1 > x2:
                rng = range(x2, x1 + 1)
            if x2 > x1:
                rng = range(x1, x2 + 1)
            points += [(r, slope * r + intercept) for r in rng]

    return points


def populate_map(all_points, include_diagonal=False):
    point_map = defaultdict(int)
    for points in all_points:
        points_between = find_points_between(*points, include_diagonal=include_diagonal)
        if points_between:
            for point in points_between:
                point_map[point] += 1
    return point_map


def main(filename):
    all_points = parse_data(filename)

    print("Part One:")
    point_map = populate_map(all_points, False)
    print(len([v for v in point_map.values() if v > 1]))

    print("Part Two:")
    point_map = populate_map(all_points, True)
    print(len([v for v in point_map.values() if v > 1]))


if __name__ == "__main__":
    main(sys.argv[1])
