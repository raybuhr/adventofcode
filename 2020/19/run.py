from aocd import get_data
import re


def parse_data(data):
    rules, msgs = data.split("\n\n")
    rules = {k: v for k, v in [r.split(": ") for r in rules.splitlines()]}
    msgs = msgs.splitlines()
    return rules, msgs


def get_re(rule, rules, part_b=False):
    """Help from:
    - Part A) https://www.youtube.com/watch?v=X-oielWtL1A
    - Part B) https://github.com/sophiebits/adventofcode/blob/main/2020/day19.py
    """
    if part_b:
        if rule == "8":
            return get_re("42", rules) + "+"
        if rule == "11":
            a = get_re("42", rules)
            b = get_re("31", rules)
            inner_part = "|".join(f"{a}{{{n}}}{b}{{{n}}}" for n in range(1, 20))
            return f"({inner_part})"
    rs = rules[rule]
    if rs.startswith('"'):
        return rs.strip('"')
    else:
        parts = rs.split()
        inner_part = "".join(
            "|" if part == "|" else get_re(part, rules, part_b) for part in parts
        )
        return f"({inner_part})"


def solve(data, part_b=False):
    rules, msgs = parse_data(data)
    regex_0 = re.compile(get_re("0", rules, part_b=part_b))
    count = 0
    for msg in msgs:
        if regex_0.fullmatch(msg):
            count += 1
    return count


def solve_part_a(data):
    return solve(data, False)


def solve_part_b(data):
    return solve(data, True)


if __name__ == "__main__":
    data = get_data(year=2020, day=19)
    print("-" * 20)
    print("Part 1:")
    a = solve_part_a(data)
    print(a)
    print("-" * 20)
    print("Part 2:")
    b = solve_part_b(data)
    print(b)
