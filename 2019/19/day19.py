import numpy as np
from aocd import get_data
from intcode import Intcode


def check_beam(data, x, y):
    ic = Intcode(data, input_queue=[x, y])
    ic.run()
    return ic.output_queue.pop()


def build_grid(data, rows, cols):
    grid = []
    for y in range(rows):
        grid.append([check_beam(data, x, y) for x in range(cols)])
    return np.array(grid)


def print_grid(grid):
    beam = {0: ".", 1: "#"}
    gridlist = grid.tolist()
    rows, cols = grid.shape
    board = [["" for _ in range(cols)] for _ in range(rows)]
    for j, row in enumerate(gridlist):
        for i, col in enumerate(row):
            board[j][i] = beam[col]
    board = "\n".join(["".join(row) for row in board])
    print(board)


def find_largest_square(n, data):
    col = [y for y in range(n) if check_beam(data, n, y)]
    if len(col) < 1:
        return 0.0
    row = [x for x in range(n+1) if check_beam(data, x, col[0])]
    if len(row) < 1:
        return 1.0
    h = len(col)
    w = len(row)
    return np.ceil((h*w)/(h+w))


def search_for_square(size, data, debug=False):
    assert size > 0
    low, high = size, size//2*size
    while (high - low) > 1:
        f = (low + high) // 2
        r = find_largest_square(f, data)
        if debug:
            print(low, high, f, r)
        if r < size:
            low = f
        else:
            high = f
    if find_largest_square(low, data) < size:
        return high
    return low


def solve_part1(grid):
    return grid.sum()


def solve_part2(data):
    n = search_for_square(100, data)
    col = [y for y in range(n) if check_beam(data, n, y)]
    row = [x for x in range(n+1) if check_beam(data, x, col[0])]
    y = col[0]
    x = row[-100]
    return 10_000 * x + y


if __name__ == "__main__":
    data = get_data(year=2019, day=19)
    grid = build_grid(data, 50, 50)
    print("-" * 20, "Part 1:", "-" * 20)
    print(solve_part1(grid), "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    print(solve_part2(data), "\n")
