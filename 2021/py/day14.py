import sys
from collections import Counter, defaultdict


def read_data(filename):
    with open(filename) as file:
        data = file.read().splitlines()
    template = data[0]
    pairs = [d.split(" -> ") for d in data[2:]]
    rules = {p[0]: p[1] for p in pairs}
    return template, rules


def step(pairs, rules, counts):
    new_pairs = defaultdict(int)
    for pair, ct in pairs.items():
        match = rules[pair]
        counts[match] += ct
        left, right = pair[0] + match, match + pair[1]
        new_pairs[left] += ct
        new_pairs[right] += ct
    return new_pairs


def apply_steps(pairs, rules, counts, n_steps):
    for _ in range(n_steps):
        pairs = step(pairs, rules, counts)


def quantity_range(counts):
    most_common = counts.most_common()
    return most_common[0][1] - most_common[-1][1]


def process(filename, n_steps):
    template, rules = read_data(filename)
    pairs = {template[i - 1 : i + 1]: 1 for i in range(1, len(template))}
    counts = Counter(template)
    apply_steps(pairs, rules, counts, n_steps)
    return quantity_range(counts)


if __name__ == "__main__":
    filename = sys.argv[1]
    print("Part One")
    print(process(filename, 10))
    print("Part Two")
    print(process(filename, 40))
