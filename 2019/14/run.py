from aocd import get_data
from collections import defaultdict
import math
import pytest


def parse_reactions(data):
    reactions = {
        right.split()[1]: (int(right.split()[0]), left)
        for left, right in [line.split(" => ") for line in data.splitlines()]
    }
    return reactions


def run_reactions(reactions, fuel_needed=1):
    counts = defaultdict(int)
    counts["FUEL"] = fuel_needed
    done = False
    while not done:
        results = defaultdict(int)
        requirements = defaultdict(int)
        for k, v in counts.items():
            results[k] = reactions[k][0] * v
            for ingredient in reactions[k][1].split(", "):
                amt, item = ingredient.split()
                requirements[item] += v * int(amt)
        print(requirements)
        for item, amt in requirements.items():
            if item == "ORE":
                ore = amt
            elif results[item] < amt:
                counts[item] += int(
                    math.ceil((amt - results[item]) / reactions[item][0])
                )
        done = all([results[i] >= requirements[i] for i in requirements if i != "ORE"])
    return ore


def solve_part1(reactions):
    return run_reactions(reactions, 1)


def solve_part2(reactions):
    ore = 1000000000000
    lo, hi = 1, ore
    while (hi - lo) > 1:
        f = (lo + hi) // 2
        r = run_reactions(reactions, f)
        # print(lo, hi, f, r < ore, r, ore)
        if r == ore:
            return f
        elif r < ore:
            lo = f
        else:
            hi = f
    return lo


test_cases = [
    (
        """9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL""",
        165,
    ),
    (
        """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT""",
        13312,
    ),
    (
        """2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF""",
        180697,
    ),
    (
        """171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX""",
        2210736,
    ),
]


@pytest.mark.parametrize("test_data,expected", test_cases)
def test_run_reactions(test_data, expected):
    test_reactions = parse_reactions(test_data)
    assert expected == run_reactions(test_reactions)


if __name__ == "__main__":
    data = get_data(year=2019, day=14)
    reactions = parse_reactions(data)
    print("-" * 20, "Part 1:", "-" * 20)
    print(solve_part1(reactions), "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    print(solve_part2(reactions))
