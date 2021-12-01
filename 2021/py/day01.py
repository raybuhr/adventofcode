from aocd import get_data
import pandas as pd


def parse_data():
    data = get_data(year=2021, day=1)
    return pd.DataFrame({"seq": [int(line) for line in data.splitlines()]})


def part_one(df):
    df["inc"] = df["seq"] > df["seq"].shift(1)
    return df["inc"].sum()


def part_two(df):
    df["window"] = df["seq"].rolling(3).sum()
    df["inc"] = df["window"] > df["window"].shift(1)
    return df["inc"].sum()


if __name__ == "__main__":
    df = parse_data()
    print("*" * 10, "Part One", "*" * 10)
    print(part_one(df))
    print("*" * 10, "Part Two", "*" * 10)
    print(part_two(df))
