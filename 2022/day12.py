from string import ascii_lowercase
import networkx

with open("input.txt") as f:
    lines = f.read().splitlines()


test_lines = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".splitlines()


heights = {a: i for i, a in enumerate(ascii_lowercase)}
heights["S"] = 0
heights["E"] = 25


def find_position(lines, marker):
    for r, row in enumerate(lines):
        for c, col in enumerate(row):
            if col == marker:
                return r, c


def build_graph(lines):
    graph = networkx.DiGraph()
    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            height = heights[lines[row][col]]
            neighbors = [
                (row + 1, col),
                (row, col + 1),
                (row - 1, col),
                (row, col - 1),
            ]
            for y, x in neighbors:
                if y < 0 or x < 0 or y >= len(lines) or x >= len(line):
                    continue
                neighbor_height = heights[lines[y][x]]
                if neighbor_height - height <= 1:
                    graph.add_edge((row, col), (y, x))
    return graph


def solve(lines):
    graph = build_graph(lines)
    start = find_position(lines, "S")
    end = find_position(lines, "E")
    shortest = networkx.shortest_path_length(graph, start, end)
    print("part a:", shortest)

    all_starting_positions = []
    for row, line in enumerate(lines):
        for col, val in enumerate(line):
            if val == "a":
                all_starting_positions.append((row, col))

    for position in all_starting_positions:
        try:
            length = networkx.shortest_path_length(graph, position, end)
        except:
            pass
        if length < shortest:
            shortest = length

    print("part b:", shortest)


solve(lines)
