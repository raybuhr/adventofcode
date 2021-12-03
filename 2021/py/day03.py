from aocd import get_data
import pandas as pd


def parse_data():
    raw_data = get_data(year=2021, day=3)
    data = [[n for n in line] for line in raw_data.splitlines()]
    return pd.DataFrame(data)


def part_one(data):
    gamma = ''.join([data[i].value_counts().idxmax() for i in data.columns])
    epsilon = ''.join([data[i].value_counts().idxmin() for i in data.columns])
    return int(gamma, 2) * int(epsilon, 2)


def oxygen_generator(data):
    df = data.copy()
    for i in df.columns:
        df = df[df[i] == df[i].value_counts().idxmax()]
        if len(df) == 1:
            break
    return ''.join(df.values[0])


def co2_scrubber(data):
    df = data.copy()
    for i in data.columns:
        df = df[df[i] != df[i].value_counts().idxmax()]
        if len(df) == 1:
            break
    return ''.join(df.values[0])


def part_two(data):
    oxygen_rating = oxygen_generator(data)
    co2_rating = co2_scrubber(data)
    return int(oxygen_rating, 2) * int(co2_rating, 2)


if __name__ == "__main__":
    data = parse_data()
    print("*" * 10, "Part One", "*" * 10)
    print(part_one(data))
    print("*" * 10, "Part Two", "*" * 10)
    print(part_two(data))

