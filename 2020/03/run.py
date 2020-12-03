from aocd import get_data
import numpy as np


def parse_data(data):
    return data.splitlines()


def find_trees_encountered(data, slope_x, slope_y):
    trees = parse_data(data)
    def step(x, y):
        return x+slope_x, y+slope_y
    
    def check_for_tree(x, y):
        if trees[y][x] == "#":
            return True
        return False
    
    x, y = 0, 0
    seen = 0
    width = len(trees[0])
    while y < len(trees) - 1:
        x, y = step(x, y)
        if x >= width:
            x -= width
        if check_for_tree(x, y):
            seen += 1

    return seen


def solve_pt2(data):
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    trees_encountered = {}
    for slope in slopes:
        trees_encountered[slope] = find_trees_encountered(data, slope[0], slope[1])
    return np.prod(list(trees_encountered.values()))


if __name__ == "__main__":
    data = get_data(year=2020, day=3)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = find_trees_encountered(data, 3, 1)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")

