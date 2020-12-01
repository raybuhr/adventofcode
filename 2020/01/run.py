from aocd import get_data
from functools import reduce
from itertools import combinations


def parse_data(data):
    return [int(i) for i in data.splitlines()]


def solve_part1(data, sum_to_num=2020):
    nums = parse_data(data)
    for x, y in combinations(nums, 2):
        if x + y == sum_to_num:
            print(x, "*", y, "=", x*y)
            return x, y


def solve_part2(data, sum_to_num=2020):
    nums = parse_data(data)
    for x, y, z in combinations(nums, 3):
        if x + y + z == sum_to_num:
            print(x, "*", y, "*", z, "=", x*y*z)
            return x, y, z


def solve(data, sum_to_num=2020, num_combinations=2):
    nums = parse_data(data)
    for c in combinations(nums, num_combinations):
        if sum(c) == sum_to_num:
            return c


def prod(nums):
    return reduce(lambda x, y: x*y, nums)


if __name__ == "__main__":
    data = get_data(year=2020, day=1)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve(data, 2020, 2)
    print(pt_1, "\n", prod(pt_1))

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve(data, 2020, 3)
    print(pt_2, "\n", prod(pt_2))

