from aocd import get_data
from collections import defaultdict
from itertools import cycle


def solve_pt1(data, turns=2021):
    nums = [int(x) for x in data.split(',')]
    said = defaultdict(list)
    counts = defaultdict(int)
    turn = 1
    for num in nums:
        last_said = num
        counts[last_said] += 1
        said[last_said] += [turn]
        turn += 1
    while turn < turns:
        if counts[last_said] < 2:
            last_said = 0
        else:
            last_said = said[last_said][-1] - said[last_said][-2]
        counts[last_said] += 1
        said[last_said] += [turn]
        turn += 1
    return last_said


def solve_pt2(data):
    return solve_pt1(data, turns=30000001)


if __name__ == "__main__":
    data = get_data(year=2020, day=15)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_pt1(data)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")
