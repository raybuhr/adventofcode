import numpy as np

with open("input.txt") as f:
    lines = f.read().splitlines()
    grid = np.array([[int(s) for s in line] for line in lines])


def find_visible(arr):
    cur_max = -1
    visible = []
    for i, val in enumerate(arr):
        if val > cur_max:
            visible.append(i)
            cur_max = val
    return visible


def find_visible_reverse(arr):
    L = len(arr)
    visible = find_visible(arr[::-1])
    return [L - i - 1 for i in visible]


def find_all_visible(grid):
    left = [find_visible(grid[i, :]) for i in range(len(grid))]
    right = [find_visible_reverse(grid[i, :]) for i in range(len(grid))]
    top = [find_visible(grid[:, i]) for i in range(len(grid))]
    bottom = [find_visible_reverse(grid[:, i]) for i in range(len(grid))]
    visible = np.zeros(grid.shape)
    for row, vis in enumerate(left):
        for col in vis:
            visible[row, col] = 1
    for row, vis in enumerate(right):
        for col in vis:
            visible[row, col] = 1
    for col, vis in enumerate(top):
        for row in vis:
            visible[row, col] = 1
    for col, vis in enumerate(bottom):
        for row in vis:
            visible[row, col] = 1
    # set outside visible
    visible[0, :] = 1
    visible[:, 0] = 1
    visible[-1, :] = 1
    return visible.sum()


print(f"part a {find_all_visible(grid):.0f}")


def look_left(grid, row, col):
    h = grid[row, col]
    see = 0
    while True:
        col -= 1
        if col < 0:
            break
        if grid[row, col] < h:
            see += 1
        else:
            see += 1
            break
    return see if see > 0 else 1


def look_right(grid, row, col):
    h = grid[row, col]
    L = len(grid)
    see = 0
    while True:
        col += 1
        if col >= L:
            break
        if grid[row, col] < h:
            see += 1
        else:
            see += 1
            break
    return see if see > 0 else 1


def look_up(grid, row, col):
    h = grid[row, col]
    see = 0
    while True:
        row -= 1
        if row < 0:
            break
        if grid[row, col] < h:
            see += 1
        else:
            see += 1
            break
    return see if see > 0 else 1


def look_down(grid, row, col):
    h = grid[row, col]
    L = len(grid)
    see = 0
    while True:
        row += 1
        if row >= L:
            break
        if grid[row, col] < h:
            see += 1
        else:
            see += 1
            break
    return see if see > 0 else 1


def calc_scenic_score(grid, row, col):
    up = look_up(grid, row, col)
    down = look_down(grid, row, col)
    left = look_left(grid, row, col)
    right = look_right(grid, row, col)
    return up * down * left * right


print(
    "part b",
    max(
        calc_scenic_score(grid, r, c)
        for r in range(len(grid))
        for c in range(len(grid))
    ),
)
