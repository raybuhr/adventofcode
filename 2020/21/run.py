from aocd import get_data
from collections import Counter, defaultdict


def get_allergen_list(data):
    allergens = []
    for line in data.splitlines():
        allergens += line.split("contains ")[-1].replace(")", "").split(", ")
    return list(set(allergens))


def possible_ingredients(allergen, data):
    ings = defaultdict(int)
    for line in data.splitlines():
        if " " + allergen in line:
            for ing in line.split("(")[0].split():
                ings[ing] += 1
    return {ing for ing, ct in ings.items() if ct == max(ings.values())}


def solve(data):
    allergens = get_allergen_list(data)
    allergen_possibilities = {a: possible_ingredients(a, data) for a in allergens}
    known = {}
    while not all(a in known for a in allergens):
        for a in allergen_possibilities:
            if len(allergen_possibilities[a]) == 1:
                known[a] = allergen_possibilities[a].pop()
        allergen_possibilities = {
            a: [p for p in ps if p not in known.values()]
            for a, ps in allergen_possibilities.items()
            if a not in known
        }
    ingredient_counter = defaultdict(int)
    for line in data.splitlines():
        for ing in line.split("(")[0].split():
            if ing not in known.values():
                ingredient_counter[ing] += 1
    pt_1 = sum(ingredient_counter.values())
    pt_2 = ",".join([known[k] for k in sorted(known)])
    return pt_1, pt_2


if __name__ == "__main__":
    data = get_data(year=2020, day=21)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1, pt_2 = solve(data)
    print(pt_1, "\n")
    print("-" * 20, "Part 2:", "-" * 20)
    print(pt_2, "\n")
