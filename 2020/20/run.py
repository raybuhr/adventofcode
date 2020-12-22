from aocd import get_data
import numpy as np
import re


def parse_data(data):
    tile_lines = data.split("\n\n")
    tiles = {}
    for tile in tile_lines:
        lines = tile.split("\n")
        tile_id = int(lines[0].replace(":", "").split()[-1])
        tiles[tile_id] = np.array([list(l) for l in lines[1:]])
    return tiles


def find_edges(mat):
    edges = []
    for i in range(8):
        if i % 4:
            mat = np.rot90(mat)
        else:
            mat = mat.T
        edges.append("".join(mat[0, :]))
    return edges


def find_matches(tile_id, edges):
    matches = []
    for tid, edgs in edges.items():
        if tid == tile_id:
            continue
        for edg in edgs:
            if edg in edges[tile_id]:
                matches.append(tid)
    return set(matches)


def setup(data):
    tiles = parse_data(data)
    edges = {k: find_edges(v) for k, v in tiles.items()}
    matches = {k: find_matches(k, edges) for k, v in edges.items()}
    corners = [k for k, v in matches.items() if len(v) == 2]
    return tiles, edges, matches, corners


def solve_pt1(data):
    tiles, edges, matches, corners = setup(data)
    return np.prod(corners)


def solve_pt2(data):
    tiles, edges, matches, corners = setup(data)
    grid = np.zeros((12, 12))

    def find_options(tile_id):
        return [m for m in matches[tile_id] if m not in grid.reshape((-1, 1))]

    start = corners[0]
    grid[0, 0] = start
    n = find_options(start)[0]
    grid[0, 1] = n
    row, col = 0, 2
    # fill top row
    while col < grid.shape[1]:
        n = [o for o in find_options(n) if len(find_options(o)) <= 2][0]
        grid[row, col] = n
        col += 1
    # fill in rest of grid
    for row in range(1, 12):
        for col in range(12):
            n = find_options(grid[row - 1, col])[0]
            grid[row, col] = n

    # fits the tiles together
    def align_tiles_left_right(tile_a, tile_b):
        common_edges = [e for e in edges[tile_a] if e in edges[tile_b]]
        aligned = "".join(tiles[tile_a][:, -1]) in common_edges
        while not aligned:
            tiles[tile_a] = np.rot90(tiles[tile_a])
            aligned = "".join(tiles[tile_a][:, -1]) in common_edges
        aligned = "".join(tiles[tile_b][:, 0]) in common_edges
        while not aligned:
            tiles[tile_b] = np.rot90(tiles[tile_b])
            aligned = "".join(tiles[tile_b][:, 0]) in common_edges
        if not all(tiles[tile_a][:, -1] == tiles[tile_b][:, 0]):
            tiles[tile_b] = np.flipud(tiles[tile_b])
        return all(tiles[tile_a][:, -1] == tiles[tile_b][:, 0])

    def align_tiles_top_bottom(tile_a, tile_b):
        common_edges = [e for e in edges[tile_a] if e in edges[tile_b]]
        aligned = "".join(tiles[tile_b][0, :]) in common_edges
        while not aligned:
            tiles[tile_b] = np.rot90(tiles[tile_b])
            aligned = "".join(tiles[tile_b][0, :]) in common_edges
        if not all(tiles[tile_a][-1, :] == tiles[tile_b][0, :]):
            tiles[tile_b] = np.fliplr(tiles[tile_b])
        return all(tiles[tile_a][-1, :] == tiles[tile_b][0, :])

    # align top row
    for i in range(11):
        align_tiles_left_right(*grid[0, i : i + 2])
    # align left column of grid
    for i in range(11):
        align_tiles_top_bottom(*grid[i : i + 2, 0])
    # align rest of grid
    for i in range(1, 11):
        for j in range(1, 11):
            align_tiles_left_right(*grid[i, j : j + 2])
    for i in range(1, 11):
        for j in range(1, 11):
            align_tiles_top_bottom(*grid[j : j + 2, i])

    tile_grid = [list("." * 12) for _ in range(12)]
    for row in range(12):
        for col in range(12):
            tile_grid[row][col] = [
                "".join(row) for row in tiles[grid[row, col]][1:-1, 1:-1]
            ]

    image = []
    for outer_row in range(len(tile_grid)):
        for inner_row in range(len(tile_grid[0][0])):
            image.append(
                "".join([tile_grid[outer_row][i][inner_row] for i in range(12)])
            )

    def rotate_image(image):
        a = np.array([list(line) for line in image])
        a = np.rot90(a)
        return ["".join(line) for line in a]

    def flip_image(image):
        a = np.array([list(line) for line in image])
        return ["".join(line) for line in a.T]

    def find_monsters(image):
        p1 = "#.{4}##.{4}##.{4}###"
        p2 = ".{1}#.{2}#.{2}#.{2}#.{2}#.{2}#.{3}"
        p1_matches, p2_matches = [], []
        for i, line in enumerate(image):
            matches = re.findall(p1, line)
            if matches:
                p1_matches += [(i, m) for m in matches]
            matches = re.findall(p2, line)
            if matches:
                p2_matches += [(i, m) for m in matches]
        return [
            (l, idx) for l, idx in p1_matches if l + 1 in [l for l, idx in p2_matches]
        ]

    found = 0
    tries = 0
    while found <= 0:
        monsters = find_monsters(image)
        if len(monsters) > 0:
            found = len(monsters)
        else:
            image = rotate_image(image)
            tries += 1
        if tries % 4 == 0:
            image = flip_image(image)

    total = sum(line.count("#") for line in image)
    return total - found * 15  # each monster has 15 #


if __name__ == "__main__":
    data = get_data(year=2020, day=20)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_pt1(data)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")
