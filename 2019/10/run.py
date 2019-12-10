from aocd.models import Puzzle
import numpy as np
from intcode import Intcode

def get_data(year, day):
    puzzle = Puzzle(year=year, day=day)
    data = puzzle.input_data
    return data


def build_spacemap(data):
    lines = data.splitlines()
    grid = [[l for l in line] for line in lines]
    return grid


def find_distance_to_point(point_a, point_b):
    return [point_a[0] - point_b[0], point_a[1] - point_b[1]]


def is_blocked(dist_a, dist_b):
    big = max(dist_a, dist_b)
    lil = min(dist_a, dist_b)
    multiple = np.array(big) / np.array(lil)
    is_multiple = all([i == int(i) for i in multiple])
    return is_multiple


def find_asteroids(spacemap):
    asteroids = []
    for r, row in enumerate(spacemap):
        for c, col in enumerate(row):
            if col == "#":
                asteroids.append([r, c])
    return asteroids


def find_visible_asteroids(point, spacemap):
    asteroids = find_asteroids(spacemap)
    # remove starting point
    for i, a in enumerate(asteroids):
        if a == point:
            asteroids.pop(i)
    distances = [
        find_distance_to_point(point, asteroids[i])
        for i in range(len(asteroids))
    ]
    count = 0
    return count


test_case1 = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""

test_case2 = """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###."""

test_case3 = """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#.."""

test_case4 = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##"""


if __name__ == "__main__":
    data = get_data()
    print("-"*20, "Part 1:", "-"*20)
    print(solve_part1(data, [1]), "\n")

    print("-"*20, "Part 2:", "-"*20)
    print(solve_part1(data, [2]), "\n")

