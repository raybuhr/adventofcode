from aocd.models import Puzzle
import numpy as np
import pytest


def get_data(year, day):
    puzzle = Puzzle(year=year, day=day)
    data = puzzle.input_data
    return data


def build_spacemap(data):
    lines = data.splitlines()
    grid = [[l for l in line] for line in lines]
    return np.array(grid)


def find_distance_between_points(point_a, point_b):
    return np.array([point_a[0] - point_b[0], point_a[1] - point_b[1]])


def find_slope_between_points(point_a, point_b):
    dist = find_distance_between_points(point_a, point_b)
    return np.arctan2(dist[0], dist[1])


def find_asteroids(spacemap):
    asteroids = []
    for r, row in enumerate(spacemap):
        for c, col in enumerate(row):
            if col == "#":
                asteroids.append((r, c))
    return asteroids


def find_visible_asteroids(point, spacemap):
    asteroids = find_asteroids(spacemap)
    # remove starting point
    for i, a in enumerate(asteroids):
        if a == point:
            asteroids.pop(i)
    slopes = {find_slope_between_points(point, a) for a in asteroids}
    return slopes


def solve_part1(spacemap):
    asteroids = find_asteroids(spacemap)
    visible_asteroids = {
        tuple(a): len(find_visible_asteroids(a, spacemap)) for a in asteroids
    }
    most = max(visible_asteroids.values())
    best = {a: v for a, v in visible_asteroids.items() if v == most}
    return best


def shoot_laser(point, spacemap):
    # find all asteroids
    asteroids = find_asteroids(spacemap)
    # remove starting point
    asteroids.pop(asteroids.index(point))

    positions = [
        (r, c)
        for r, row in enumerate(spacemap)
        for c, col in enumerate(row)
        if (r, c) != point
    ]
    slopes = {p: find_slope_between_points(point, p) for p in positions}

    def get_next_slope(slope_at, slopes):
        try:
            next_slope = min(v for v in slopes.values() if v > slope_at)
        except:
            next_slope = min(v for v in slopes.values())
        return next_slope

    # start counter
    slope_at = slopes[(0, point[1])]
    counter = 1
    shots = {}
    while counter <= 200:
        visible_points = {p: s for p, s in slopes.items() if s == slope_at}
        visible_asteroids = [p for p in visible_points if p in asteroids]
        if len(visible_asteroids) < 1:
            slope_at = get_next_slope(slope_at, slopes)
            continue
        distances = {
            sum(find_distance_between_points(point, p)): p for p in visible_asteroids
        }
        best = distances[min(distances)]
        shots[counter] = asteroids.pop(asteroids.index(best))
        counter += 1
        slope_at = get_next_slope(slope_at, slopes)
    return shots


def solve_part2(point, spacemap):
    shots = shoot_laser(point, spacemap)
    y, x = shots[200]
    return x * 100 + y


test_cases = [
    (
        """.#..#
.....
#####
....#
...##""",
        {(4, 3): 8},
    ),
    (
        """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####""",
        {(8, 5): 33},
    ),
    (
        """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.""",
        {(2, 1): 35},
    ),
    (
        """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..""",
        {(3, 6): 41},
    ),
    (
        """.#..##.###...#######
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
###.##.####.##.#..##""",
        {(13, 11): 210},
    ),
]


@pytest.mark.parametrize("test_data,expected", test_cases)
def test_solve_part1(test_data, expected):
    spacemap = build_spacemap(test_data)
    got = solve_part1(spacemap)
    assert expected == got


def test_solve_part2():
    spacemap = build_spacemap(test_cases[-1][0])
    position, _ = test_cases[-1][1].popitem()
    assert solve_part2(position, spacemap) == 802


if __name__ == "__main__":
    data = get_data(year=2019, day=10)
    spacemap = build_spacemap(data)
    print("-" * 20, "Part 1:", "-" * 20)
    best = solve_part1(spacemap)
    position, solution = best.popitem()
    print(solution, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    print(solve_part2(position, spacemap), "\n")
