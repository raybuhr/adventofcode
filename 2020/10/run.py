from aocd import get_data
import numpy as np
import pandas as pd


def parse_data(data):
    d = pd.Series(data.splitlines()).astype(int)
    s = pd.Series([0, max(d) + 3])
    return d.append(s).sort_values()


def solve_pt1(data):
    d = parse_data(data)
    s = (d - d.shift(1)).value_counts()
    return np.prod(s)


def solve_pt2(data):
    # path_map is a lookup for how many paths exist between a string of consecutive numbers
    path_map = {1: 1, 2: 1, 3: 2, 4: 4, 5: 7}
    df = parse_data(data).to_frame("jolts")
    df["diffs"] = df["jolts"] - df["jolts"].shift(1)
    df["batch"] = (df["diffs"] == 3).cumsum()
    runs = df.groupby("batch")["jolts"].count()
    return runs.map(path_map).cumprod().max()


def solve_with_dynamic_programming(data):
    jolts = sorted([int(i) for i in data.splitlines()])
    arrangements = {0: 1}
    for j in jolts:
        arrangements[j] = (
            arrangements.get(j - 1, 0)
            + arrangements.get(j - 2, 0)
            + arrangements.get(j - 3, 0)
        )
    return arrangements[j]


if __name__ == "__main__":
    data = get_data(year=2020, day=10)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_pt1(data)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")
