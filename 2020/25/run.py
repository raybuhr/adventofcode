from aocd import get_data


def handshake(num, loop_size):
    denom = 20201227
    value = 1
    for _ in range(loop_size):
        value = (value * num) % denom
    return value


def crack_loop_size(key):
    value = 1
    denom = 20201227
    num = 7
    loop = 0
    while True:
        loop += 1
        value = (value * num) % denom
        if value == key:
            return loop


def solve_part_a(data):
    a, b = [int(d) for d in data.splitlines()]
    a_loop_size = crack_loop_size(a)
    b_loop_size = crack_loop_size(b)
    return handshake(a, b_loop_size)


def solve_part_b(data):
    pass


if __name__ == "__main__":
    data = get_data(year=2020, day=25)
    print("Part 1:")
    a = solve_part_a(data)
    print(a)
    print("Part 2:")
    b = solve_part_b(data)
    print(b)

