from aocd import get_data
from collections import defaultdict
from itertools import product


def make_grid_3d(data):
    rows = data.splitlines()
    grid = {}
    for y, row in enumerate(rows):
        for x, col in enumerate(row):
            grid[(x, y, 0)] = 1 if col == "#" else 0
    return grid
    

def find_neighbors_3d(x, y, z):
    shift = list(product((-1,0,1), (-1,0,1), (-1,0,1)))
    neighbors = [(x+s[0], y+s[1], z+s[2]) for s in shift if s != (0,0,0)]
    return neighbors


def activate_3d(grid, x, y, z):
    active = sum(grid.get(n, 0) for n in find_neighbors_3d(x, y, z))
    state = grid.get((x,y,z), 0)
    if (state == 1 and 2 <= active <= 3) or (state == 0 and active == 3):
        return 1
    return 0


def solve_pt1(data, cycles=6):
    grid = make_grid_3d(data)
    for i in range(cycles):
        neighbors = []
        for coord in grid:
            neighbors += find_neighbors_3d(*coord)
        for n in set(neighbors):
            if n not in grid:
                grid[n] = 0
        new_grid = {}
        for coord in grid:
            new_grid[coord] = activate_3d(grid, *coord)
        grid = new_grid
    return sum(grid.values())


def make_grid_4d(data):
    rows = data.splitlines()
    grid = {}
    for y, row in enumerate(rows):
        for x, col in enumerate(row):
            grid[(x, y, 0, 0)] = 1 if col == "#" else 0
    return grid
    

def find_neighbors_4d(x, y, z, w):
    shift = list(product((-1,0,1), (-1,0,1), (-1,0,1), (-1,0,1)))
    neighbors = [(x+s[0], y+s[1], z+s[2], w+s[3]) for s in shift if s != (0,0,0,0)]
    return neighbors


def activate_4d(grid, x, y, z, w):
    active = sum(grid.get(n, 0) for n in find_neighbors_4d(x, y, z, w))
    state = grid.get((x,y,z,w), 0)
    if (state == 1 and 2 <= active <= 3) or (state == 0 and active == 3):
        return 1
    return 0


def solve_pt2(data, cycles=6):
    grid = make_grid_4d(data)
    for i in range(cycles):
        neighbors = []
        for coord in grid:
            neighbors += find_neighbors_4d(*coord)
        for n in set(neighbors):
            if n not in grid:
                grid[n] = 0
        new_grid = {}
        for coord in grid:
            new_grid[coord] = activate_4d(grid, *coord)
        grid = new_grid
    return sum(grid.values())


if __name__ == "__main__":
    data = get_data(year=2020, day=17)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_pt1(data)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")
