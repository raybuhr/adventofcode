from aocd import get_data
from collections import Counter


def parse_data(data):
    return [d.splitlines() for d in data.split("\n\n")]


def count_group_answers(group):
    return len(set("".join(group)))


def count_same_answers(group):
    answers = "".join(group)
    counts = Counter(answers)
    return len([v for v in counts.values() if v == len(group)])


def solve_pt1(data):
    return sum(count_group_answers(d) for d in parse_data(data))


def solve_pt2(data):
    return sum(count_same_answers(d) for d in parse_data(data))


if __name__ == "__main__":
    data = get_data(year=2020, day=6)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_pt1(data)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")
