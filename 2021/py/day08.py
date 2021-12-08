import sys


def read_data(filename):
    with open(filename) as file:
        text = file.read()
    return text.splitlines()


def part_one(lines):
    counter = 0
    for line in lines:
        left, right = line.split(" | ")
        for word in right.split(" "):
            if word == "|":
                continue
            if len(word) < 5 or len(word) > 6:
                counter += 1
    return counter


def wire_to_digit(wire):
    mapper = {2: 1, 3: 7, 4: 4, 7: 8, 5: [2, 3, 5], 6: [0, 6, 9]}
    return mapper[len(wire)]


def build_wire_map(line):
    words = line.replace(" |", "").split(" ")
    wire_map = {i: [] for i in range(10)}

    for word in words:
        word = "".join(sorted(word))
        digit = wire_to_digit(word)
        if type(digit) == int:
            wire_map[digit] = word
        else:
            for d in digit:
                if word not in wire_map[d]:
                    wire_map[d].append(word)

    return wire_map


def decode_line(line):
    wire_map = build_wire_map(line)
    one = wire_map[1]
    for wire in wire_map[6]:
        if not all(w in wire for w in one):
            six = wire
    wire_map[6] = six
    wire_map[9] = [wire for wire in wire_map[9] if wire != six]
    for wire in wire_map[9]:
        if all(w in wire for w in wire_map[4]):
            nine = wire
    wire_map[9] = nine
    wire_map[0] = [wire for wire in wire_map[0] if wire not in [six, nine]].pop()
    for wire in wire_map[3]:
        if all(w in wire for w in one):
            three = wire
    wire_map[3] = three
    for wire in wire_map[5]:
        if wire != three and all(w in wire_map[6] for w in wire):
            five = wire
    wire_map[5] = five
    wire_map[2] = [wire for wire in wire_map[2] if wire not in [three, five]].pop()
    return {val: str(key) for key, val in wire_map.items()}


def solve_line(line):
    decoder = decode_line(line)
    output_wires = ["".join(sorted(wire)) for wire in line.split("| ")[-1].split(" ")]
    output_value = "".join(decoder[wire] for wire in output_wires)
    return int(output_value)


def part_two(lines):
    return sum(solve_line(line) for line in lines)


if __name__ == "__main__":
    filename = sys.argv[1]
    lines = read_data(filename)
    print("Part One:")
    print(part_one(lines))
    print("Part Two:")
    print(part_two(lines))
