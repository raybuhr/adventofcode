from aocd import get_data


def parse_data(data):
    return data.splitlines()


def step(code, x, y, facing):
    cmd, num = code[0], int(code[1:])
    dirs = {
        "N": (0, 1 * num),
        "S": (0, -1 * num),
        "E": (1 * num, 0),
        "W": (-1 * num, 0),
    }
    faces = {"N": -1j, "E": 1, "W": -1, "S": 1j}
    rev_faces = {v: k for k, v in faces.items()}
    turn_right = 1j
    turn_left = -1j
    d = dirs.get(cmd)
    if d:
        return d[0] + x, d[1] + y, facing
    elif cmd == "F":
        d = dirs.get(facing)
        return d[0] + x, d[1] + y, facing
    elif cmd == "R":
        times = num // 90
        for _ in range(times):
            facing = rev_faces[faces.get(facing) * turn_right]
        return x, y, facing
    elif cmd == "L":
        times = num // 90
        for _ in range(times):
            facing = rev_faces[faces.get(facing) * turn_left]
        return x, y, facing
    elif cmd == "F":
        d = dirs.get(facing)
        return d[0] + x, d[1] + y, facing
    else:
        raise Exception("bad command")


def rotate(facing, x, y):
    if facing == "R":
        return y, -1 * x
    if facing == "L":
        return -1 * y, x


def step2(code, x, y, f, wx, wy):
    c, num = code[0], int(code[1:])
    if c in "NSWE":
        wx, wy, f = step(code, wx, wy, f)
    elif c == "F":
        x += wx * num
        y += wy * num
    elif c in "RL":
        times = num // 90
        for _ in range(times):
            wx, wy = rotate(c, wx, wy)
    return x, y, f, wx, wy


def solve_pt1(data):
    codes = parse_data(data)
    x, y, f = 0, 0, "E"
    for code in codes:
        x, y, f = step(code, x, y, f)
    return abs(x) + abs(y)


def solve_pt2(data):
    codes = parse_data(data)
    x, y, f, wx, wy = 0, 0, "E", 10, 1
    for code in codes:
        x, y, f, wx, wy = step2(code, x, y, f, wx, wy)
    return abs(x) + abs(y)


if __name__ == "__main__":
    data = get_data(year=2020, day=12)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_pt1(data)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")
