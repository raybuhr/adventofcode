import math

with open("input.txt") as fp:
    data = fp.read().split("\n")


def calc_fuel(x):
    y = math.floor(x / 3) - 2
    return y


def test_calc_fuel():
    assert calc_fuel(12) == 2
    assert calc_fuel(14) == 2
    assert calc_fuel(1969) == 654
    assert calc_fuel(100756) == 33583


def calc_all_fuel(x):
    fuel = 0
    y = calc_fuel(x)
    while y > 0:
        fuel += y
        y = calc_fuel(y)
    return fuel


def test_calc_all_fuel():
    assert calc_all_fuel(12) == 2
    assert calc_all_fuel(14) == 2
    assert calc_all_fuel(1969) == 966
    assert calc_all_fuel(100756) == 50346


if __name__ == "__main__":
    fuel_required = [calc_fuel(int(d)) for d in data]
    total_fuel = sum(f for f in fuel_required)
    print("Part 1:", total_fuel, sep="\n")

    fuel_required = [calc_all_fuel(int(d)) for d in data]
    total_fuel = sum(f for f in fuel_required)
    print("Part 2:", total_fuel, sep="\n")
