from collections import defaultdict
import sys


def read_data(filename):
    with open(filename) as file:
        raw_data = file.read()
    return raw_data


def parse_data(data):
    fishes = defaultdict(int)
    for n in data.split(","):
        fishes[int(n)] += 1
    return fishes


def step(fishes):
    new_fish = defaultdict(int)
    for fish, count in fishes.items():
        if fish == 0:
            new_fish[8] += count
            new_fish[6] += count
        else:
            new_fish[fish - 1] += count
    return new_fish


def main(filename):
    fishes = parse_data(read_data(filename))
    print("Part One:")
    for day in range(80):
        fishes = step(fishes)
    print(sum(fishes.values()))
    print("Part Two:")
    for day in range(256 - 80):
        fishes = step(fishes)
    print(sum(fishes.values()))


if __name__ == "__main__":
    filename = sys.argv[1]
    print("running program for day 6 on", filename, "...")
    main(filename)
