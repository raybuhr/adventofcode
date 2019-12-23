import re
from aocd import get_data
from intcode import Intcode


def parse_scaffold(ic):
    new_lines = [i for i, v in enumerate(ic.output_queue) if v == 10]
    scaffold = []
    start = 0
    while new_lines:
        ix = new_lines.pop(0)
        row = [chr(i) for i in ic.output_queue[start:ix]]
        scaffold.append(row)
        start = ix + 1
    return [row for row in scaffold if len(row) > 0]


def solve_part1(data):
    ic = Intcode(data, input_queue=[])
    ic.run()
    scaffold = parse_scaffold(ic)
    intersections = []
    hashes = {}
    for y, row in enumerate(scaffold):
        for x, col in enumerate(row):
            if col == "#":
                hashes[(x, y)] = col

    for x, y in hashes:
        if (
            hashes.get((x + 1, y))
            and hashes.get((x - 1, y))
            and hashes.get((x, y - 1))
            and hashes.get((x, y + 1))
        ):
            intersections.append((x, y))

    return sum(x * y for x, y in intersections)


def find_next_step(hashes, position, direction):
    x, y = position
    if direction == "^":
        if hashes.get((x, y - 1)):
            return (x, y - 1), "^"
        # check right
        elif hashes.get((x + 1, y)):
            return (x + 1, y), ">"
        # check left
        elif hashes.get((x - 1, y)):
            return (x - 1, y), "<"
    if direction == "v":
        if hashes.get((x, y + 1)):
            return (x, y + 1), "v"
        # check right
        elif hashes.get((x + 1, y)):
            return (x + 1, y), ">"
        # check left
        elif hashes.get((x - 1, y)):
            return (x - 1, y), "<"
    if direction == ">":
        if hashes.get((x + 1, y)):
            return (x + 1, y), ">"
        # check up
        elif hashes.get((x, y + 1)):
            return (x, y + 1), "v"
        # check down
        elif hashes.get((x, y - 1)):
            return (x, y - 1), "^"
    if direction == "<":
        if hashes.get((x - 1, y)):
            return (x - 1, y), "<"
        # check up
        elif hashes.get((x, y + 1)):
            return (x, y + 1), "v"
        # check down
        elif hashes.get((x, y - 1)):
            return (x, y - 1), "^"


def generate_ngrams(s, n):
    # Break sentence in the token, remove empty tokens
    tokens = [token for token in s.split(" ") if token != ""]

    # Use the zip function to help us generate n-grams
    # Concatentate the tokens into ngrams and return
    ngrams = zip(*[tokens[i:] for i in range(n)])
    return [" ".join(ngram) for ngram in ngrams]


def string_to_ascii_list(string):
    return list(map(ord, list(string)))


def solve_part2(data):
    ic = Intcode("2" + data[1:], input_queue=[])
    ic.run()
    scaffold = parse_scaffold(ic)
    hashes = {}
    for y, row in enumerate(scaffold):
        for x, col in enumerate(row):
            if col == "#":
                hashes[(x, y)] = col

    trail = []
    position = (0, 10)
    direction = "^"
    while True:
        try:
            position, direction = find_next_step(hashes, position, direction)
            trail.append((position, direction))
        except:
            break

    directions = [t[1] for t in trail]
    direction_changes = [i for i, d in enumerate(directions) if d != directions[i - 1]]
    instructions = []
    for start, stop in zip(
        direction_changes, direction_changes[1:] + [len(directions)]
    ):
        dirs = directions[start:stop]
        d = dirs[0]
        c = len(dirs)
        instructions.append((d, c))

    better_instructions = []
    for i, inst in enumerate(instructions):
        d, c = inst
        if i == 0:
            pd = "^"
        else:
            pd = instructions[i - 1][0]
        if pd == "^" and d == ">":
            turn = "R"
        elif pd == "^" and d == "<":
            turn = "L"
        elif pd == "v" and d == "<":
            turn = "R"
        elif pd == "v" and d == ">":
            turn = "L"
        elif pd == ">" and d == "^":
            turn = "L"
        elif pd == ">" and d == "v":
            turn = "R"
        elif pd == "<" and d == "^":
            turn = "R"
        elif pd == "<" and d == "v":
            turn = "L"
        better_instructions.append(f"{turn}{c}")

    instructions = " ".join(better_instructions)

    main_prog = (
        instructions.replace("R8 L10 R8", "A")
        .replace("R12 R8 L8 L12", "B")
        .replace("L12 L10 L8", "C")
        .replace(" ", ",")
    ) + "\n"

    main = string_to_ascii_list(main_prog)
    A = string_to_ascii_list("R,8,L,10,R,8\n")
    B = string_to_ascii_list("R,12,R,8,L,8,L,12\n")
    C = string_to_ascii_list("L,12,L,10,L,8\n")
    video_feed = string_to_ascii_list("n\n")

    series = [main, A, B, C, video_feed]

    for s in series:
        ic.input_queue.extend(s)
        ic.run()

    return ic.output_queue[-1]


if __name__ == "__main__":
    data = get_data(year=2019, day=17)
    print("-" * 20, "Part 1:", "-" * 20)
    print(solve_part1(data), "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    print(solve_part2(data), "\n")
