from aocd import get_data
import itertools
import math
import pytest


def get_starting_positions(data):
    positions = [
        (int(a[2:]), int(b[2:]), int(c[2:]))
        for a, b, c in [p[1:-1].split(", ") for p in data.splitlines()]
    ]
    return positions


class Moon(object):
    def __init__(self, x, y, z):
        self.position = {"x": x, "y": y, "z": z}
        self.velocity = {"x": 0, "y": 0, "z": 0}

    def apply_gravity(self, other_moon):
        for i in ["x", "y", "z"]:
            if other_moon.position[i] > self.position[i]:
                self.velocity[i] += 1
                other_moon.velocity[i] -= 1
            elif other_moon.position[i] < self.position[i]:
                self.velocity[i] -= 1
                other_moon.velocity[i] += 1

    def apply_velocity(self):
        for i in ["x", "y", "z"]:
            self.position[i] += self.velocity[i]

    def calculate_potential_energy(self):
        return sum(
            [abs(self.position["x"]), abs(self.position["y"]), abs(self.position["z"])]
        )

    def calculate_kinetic_energy(self):
        return sum(
            [abs(self.velocity["x"]), abs(self.velocity["y"]), abs(self.velocity["z"])]
        )

    def calculate_total_energy(self):
        return self.calculate_potential_energy() * self.calculate_kinetic_energy()

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"position<x={self.position['x']}"
            f", y={self.position['y']}"
            f", z={self.position['z']}>"
            f", velocity<x={self.velocity['x']}"
            f", y={self.velocity['y']}"
            f", z={self.velocity['z']}>)"
        )


def solve_part1(data, steps=1000):
    starting_positions = get_starting_positions(data)
    moons = [Moon(*i) for i in starting_positions]
    for i in range(steps):
        for m1, m2 in itertools.combinations(moons, 2):
            m1.apply_gravity(m2)
        for m in moons:
            m.apply_velocity()
    energy = sum([m.calculate_total_energy() for m in moons])
    return energy


def solve_part2(data):
    starting_positions = get_starting_positions(data)
    moons = [Moon(*i) for i in starting_positions]
    positions = [[p[i] for p in starting_positions] for i in range(3)]
    steps = {}
    counter = 1
    while len(steps) < 3:
        for m1, m2 in itertools.combinations(moons, 2):
            m1.apply_gravity(m2)
        for m in moons:
            m.apply_velocity()
        cur_positions = [[m.position[i] for m in moons] for i in ["x", "y", "z"]]
        cur_velocities = [[m.velocity[i] for m in moons] for i in ["x", "y", "z"]]
        for i in range(3):
            if (
                positions[i] == cur_positions[i]
                and cur_velocities[i] == [0] * 4
                and steps.get(i) is None
            ):
                steps[i] = counter
        counter += 1

    def lcm(a, b):
        return (a * b) // math.gcd(a, b)

    return lcm(lcm(steps[0], steps[1]), steps[2])


part_one_test_cases = [
    (
        "<x=-1, y=0, z=2>\n<x=2, y=-10, z=-7>\n<x=4, y=-8, z=8>\n<x=3, y=5, z=-1>",
        10,
        179,
    ),
    (
        "<x=-8, y=-10, z=0>\n<x=5, y=5, z=10>\n<x=2, y=-7, z=3>\n<x=9, y=-8, z=-3>",
        100,
        1940,
    ),
]


@pytest.mark.parametrize("data,steps,expected", part_one_test_cases)
def test_solve_part1(data, steps, expected):
    assert solve_part1(data, steps) == expected


part_two_test_cases = [
    ("<x=-1, y=0, z=2>\n<x=2, y=-10, z=-7>\n<x=4, y=-8, z=8>\n<x=3, y=5, z=-1>", 2772),
    (
        "<x=-8, y=-10, z=0>\n<x=5, y=5, z=10>\n<x=2, y=-7, z=3>\n<x=9, y=-8, z=-3>",
        4686774924,
    ),
]


@pytest.mark.parametrize("data,expected", part_two_test_cases)
def test_solve_part1(data, expected):
    assert solve_part2(data) == expected


if __name__ == "__main__":
    data = get_data(year=2019, day=12)
    print("-" * 20, "Part 1:", "-" * 20)
    print(solve_part1(data, 1000), "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    print(solve_part2(data))
