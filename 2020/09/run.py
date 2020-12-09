from aocd import get_data
from itertools import combinations


def parse_data(data):
    return [int(i) for i in data.splitlines()]


def has_combination_of_two_that_sum_to(nums, sum_to):
    combs = combinations(nums, 2)
    return any(sum(c) == sum_to for c in combs)


def solve_part_a(data):
    nums = parse_data(data)
    for i, n in enumerate(nums[25:]):
        i += 25
        if not has_combination_of_two_that_sum_to(nums[i-25:i], n):
            return n


def solve_part_b(data):
    nums = parse_data(data)
    ans = solve_part_a(data)
    def check_window(window):
        for i, n in enumerate(nums):
            if i < window:
                continue
            a = nums[i-window:i]
            if sum(a) == ans:
                return min(a) + max(a)
    window = 2
    while window < 100:  # got to start somewhere
        res = check_window(window)
        if res:
            return res
        window += 1


if __name__ == "__main__":
    data = get_data(year=2020, day=9)
    print("-" * 20, "Part a:", "-" * 20)
    pt_1 = solve_part_a(data)
    print(pt_1)

    print("-" * 20, "Part a:", "-" * 20)
    pt_2 = solve_part_b(data)
    print(pt_2)

