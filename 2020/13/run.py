from aocd import get_data

def solve_pt1(data):
    data = data.splitlines()
    start = int(data[0])
    buses = [int(b) for b in data[1].split(",") if b != 'x']
    ts = start
    done = False
    while not done:
        for b in buses:
            if ts % b == 0:
                return (ts - start) * b
        ts += 1


def solve_pt2(data):
    data = data.splitlines()[1].split(",")
    buses = [(i, int(b)) for i, b in enumerate(data) if b != 'x']
    ts = skip = buses[0][1]
    matches = []
    for i, bus in buses[1:]:
        found = False
        while not found:
            if (ts + i) % bus == 0:
                matches.append(ts)
                found = True
            ts += skip
        ts = matches[-1]
        skip *= bus
    return matches[-1]


if __name__ == "__main__":
    data = get_data(year=2020, day=13)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_pt1(data)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")
