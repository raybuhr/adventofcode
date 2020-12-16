from aocd import get_data
import numpy as np


def parse_data(data):
    info = data.split("\n\n")
    rules, ticket, nearby = [i.splitlines() for i in info]
    rules = {rule.split(": ")[0]: rule.split(": ")[-1].split(" or ") for rule in rules}
    ticket = [int(n) for n in ticket[1].split(",")]
    nearby = [[int(n) for n in row.split(",")] for row in nearby[1:]]
    return {"rules": rules, "ticket": ticket, "nearby": nearby}


def parse_rule_nums(rule):
    a, b = rule
    a = [int(n) for n in a.split("-")]
    b = [int(n) for n in b.split("-")]
    a = list(range(a[0], a[1] + 1))
    b = list(range(b[0], b[1] + 1))
    return a + b


def determine_valid_numbers(rules):
    nums = []
    for rule in rules:
        a = parse_rule_nums(rule)
        nums += a
    return set(nums)


def solve_pt1(data):
    info = parse_data(data)
    valid = determine_valid_numbers(info["rules"].values())
    invalid = []
    for row in info["nearby"]:
        for n in row:
            if n not in valid:
                invalid.append(n)
    return sum(invalid)


def solve_pt2(data):
    info = parse_data(data)
    valid_nums = determine_valid_numbers(info["rules"].values())
    valid_tickets = []
    for row in info["nearby"]:
        if all(n in valid_nums for n in row):
            valid_tickets.append(row)
    rules = {k: set(parse_rule_nums(v)) for k, v in info["rules"].items()}
    possible = {}
    valid_tickets = np.array(valid_tickets)
    for r, nums in rules.items():
        possible[r] = [
            c
            for c in range(valid_tickets.shape[1])
            if all(n in nums for n in valid_tickets[:, c])
        ]
    labels = {}
    find = 1
    not_done = True
    while not_done:
        f = {k: v for k, v in possible.items() if len(v) <= find and k not in labels}
        if f:
            k, vals = f.popitem()
            labels.update({k: [v for v in vals if v not in labels.values()][0]})
        if len(labels) == len(possible):
            not_done = False
        find += 1
    depart_ids = [v for k, v in labels.items() if "departure" in k]
    ticket_cols = [n for i, n in enumerate(info["ticket"]) if i in depart_ids]
    return np.prod(ticket_cols)


if __name__ == "__main__":
    data = get_data(year=2020, day=16)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_pt1(data)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")
