from aocd import get_data

def parse_data(data):
    return data.splitlines()


def determine_seat_id(ticket):
    rows = list(range(128))
    seats = list(range(8))
    for i in ticket[:7]:
        if i == "F":
            rows = rows[:len(rows)//2]
        elif i == "B":
            rows = rows[len(rows)//2:]
    for i in ticket[7:]:
        if i == "L":
            seats = seats[:len(seats)//2]
        elif i == "R":
            seats = seats[len(seats)//2:]
    return rows[0] * 8 + seats[0]


def solve_pt1(data):
    return max(
        determine_seat_id(ticket)
        for ticket in parse_data(data)
    )


def solve_pt2(data):
    seats = {
        determine_seat_id(ticket)
        for ticket in parse_data(data)
    }
    return set(range(min(seats), max(seats))) - seats


if __name__ == "__main__":
    data = get_data(year=2020, day=5)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_pt1(data)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")
