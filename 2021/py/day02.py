from aocd import get_data


def parse_data():
    raw_data = get_data(year=2021, day=2)
    data = [line.split(" ") for line in raw_data.splitlines()]
    return data


def part_one(data):
    position = 0
    depth = 0

    for cmd, amt in data:
        if cmd == 'forward':
            position += int(amt)
        if cmd == 'down':
            depth += int(amt)
        if cmd == 'up':
            depth -= int(amt)

    return position * depth


def part_two(data):
    position = 0
    depth = 0
    aim = 0

    for cmd, amount in data:
        amt = int(amount)
        if cmd == 'down':
            aim += amt
        if cmd == 'up':
            aim -= amt
        if cmd == 'forward':
            position += amt
            depth += aim * amt

    return position * depth


if __name__ == "__main__":
    data = parse_data()
    print("*" * 10, "Part One", "*" * 10)
    print(part_one(data))
    print("*" * 10, "Part Two", "*" * 10)
    print(part_two(data))

