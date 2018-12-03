#!/usr/bin/env python

import itertools

with open("day6.txt") as f:
    line = f.readlines()

banks = [int(x) for x in line[0].split("\t")]

def get_max(num_list):
    current = 0
    idx = 0
    for i, v in enumerate(num_list):
        if v > current:
            current = v
            idx = i
    return idx, current

count = 0
seen = {}

while tuple(banks) not in seen:
    seen[tuple(banks)] = count
    i, m = get_max(banks)
    banks[i] = 0
    for j in itertools.islice(itertools.cycle(range(len(banks))), i + 1, i + m + 1):
        banks[j] += 1
    count += 1

print(count)
print(count - seen[tuple(banks)])
