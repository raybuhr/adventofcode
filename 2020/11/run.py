from aocd import get_data
from collections import defaultdict
from dataclasses import dataclass


def add(x1, y1, x2, y2, multiplier=1):
    return x1 + x2 * multiplier, y1 + y2 * multiplier


@dataclass
class Seats:
    data: str
    adj = [(1, 0), (-1, 0), (-1, -1), (1, -1), (0, 1), (0, -1), (1, 1), (-1, 1)]

    def parse_data(self):
        lines = self.data.splitlines()
        self.rows = len(lines)
        self.cols = len(lines[0])
        self.seats = defaultdict(str)
        for i, row in enumerate(lines):
            for j, col in enumerate(row):
                self.seats[(i, j)] = col

    def convert_seats_to_string(self):
        seat_str = []
        for y in range(self.rows):
            col_str = []
            for x in range(self.cols):
                col_str.append(self.seats[(y, x)])
            seat_str.append(col_str)
        return "\n".join(["".join(s) for s in seat_str])

    def find_open_seats(self):
        return {k for k, v in self.seats.items() if v == "L"}

    def find_filled_seats(self):
        return {k for k, v in self.seats.items() if v == "#"}

    def fill_open_seats_a(self, verbose=False):
        open_seats = self.find_open_seats()
        filled = []
        for op in open_seats:
            if all([self.seats[add(*op, *a)] != "#" for a in self.adj]):
                filled.append(op)
        for f in filled:
            self.seats[f] = "#"
        if verbose:
            print(f"Filled {len(filled)} seats")

    def leave_adjacent_seats_a(self, verbose=False):
        filled_seats = self.find_filled_seats()
        left = []
        for fs in filled_seats:
            if sum([self.seats[add(*fs, *a)] == "#" for a in self.adj]) >= 4:
                left.append(fs)
        for l in left:
            self.seats[l] = "L"
        if verbose:
            print(f"Left {len(left)} seats")

    def fill_open_seats_b(self):
        open_seats = self.find_open_seats()
        filled = []
        for op in open_seats:
            nearest = [(i, self.seats[add(*op, *a)]) for i, a in enumerate(self.adj)]
            floors = [(i, n) for i, n in nearest if n == "."]
            mult = 2
            while len(floors):
                for i, f in floors:
                    nearest[i] = (
                        i,
                        self.seats[add(*op, *self.adj[i], multiplier=mult)],
                    )
                floors = [(i, n) for i, n in nearest if n == "."]
                mult += 1
            if any(self.seats[n] == "L" for i, n in nearest):
                filled.append(op)
        for f in filled:
            self.seats[f] = "#"

    def leave_adjacent_seats_b(self):
        filled_seats = self.find_filled_seats()
        left = []
        for fs in filled_seats:
            nearest = [(i, self.seats[add(*op, *a)]) for i, a in enumerate(self.adj)]
            floors = [(i, n) for i, n in nearest if n == "."]
            mult = 2
            while len(floors):
                for i, f in floors:
                    nearest[i] = (
                        i,
                        self.seats[add(*op, *self.adj[i], multiplier=mult)],
                    )
                floors = [(i, n) for i, n in nearest if n == "."]
                mult += 1
            if sum(self.seats[n] == "#" for i, n in nearest) >= 5:
                left.append(fs)
        for l in left:
            self.seats[l] = "L"


def solve_part_a(data):
    seats = Seats(data)
    seats.parse_data()
    done = False
    counter = 0
    times_same = 0
    while not done:
        before = seats.convert_seats_to_string()
        counter += 1
        seats.fill_open_seats_a()
        seats.leave_adjacent_seats_a()
        after = seats.convert_seats_to_string()
        if before != after:
            times_same = 0
        else:
            times_same += 1
        if times_same > 3:
            done = True
    print(f"Finished after {counter} iterations")
    return len(seats.find_filled_seats())


def solve_part_b(data):
    seats = Seats(data)
    seats.parse_data()
    done = False
    counter = 0
    times_same = 0
    while not done:
        before = seats.convert_seats_to_string()
        counter += 1
        seats.fill_open_seats_b()
        seats.leave_adjacent_seats_b()
        after = seats.convert_seats_to_string()
        if before != after:
            times_same = 0
        else:
            times_same += 1
        if times_same > 3:
            done = True
    print(f"Finished after {counter} iterations")
    return len(seats.find_filled_seats())


if __name__ == "__main__":
    data = get_data(year=2020, day=11)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_part_a(data)
    print(pt_1)

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_part_b(data)
    print(pt_2)
