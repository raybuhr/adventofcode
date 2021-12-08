import numpy as np
import sys


def read_data(filename):
    with open(filename) as file:
        data = file.read().split(",")
    return np.loadtxt(data)


def part_one(data):
    med = np.median(data)
    return np.abs(data - med).sum()


def find_fuel_cost(data, position):
    dist = np.abs(data - position)
    fuel = [np.arange(1, d + 1).sum() for d in dist]
    return sum(fuel)


def part_two(data):
    avg = np.mean(data)
    left = find_fuel_cost(data, np.floor(avg))
    right = find_fuel_cost(data, np.ceil(avg))
    return min([left, right])


if __name__ == "__main__":
    data = read_data(sys.argv[1])
    print("Part One:")
    print(part_one(data))
    print("Part Two:")
    print(part_two(data))
