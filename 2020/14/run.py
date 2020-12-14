from aocd import get_data
from collections import defaultdict
from itertools import product
import re


def run_through_mask(mask, value):
    update = str(bin(value)).replace("0b", "").zfill(36)
    n = []
    for u, m in zip(update, mask):
        if m == "X":
            n.append(u)
        else:
            n.append(m)
    return int("".join(n), 2)


def solve_pt1(data):
    memory = defaultdict(int)
    lines = data.splitlines()
    for line in lines:
        if line.startswith("mask"):
            mask = line.split(" ")[-1]
        else:
            addr, value = [int(f) for f in re.findall("\d+", line)]
            memory[addr] = run_through_mask(mask, value)
    return sum(memory.values())


def decode_mask(mask, address):
    addr = str(bin(address)).replace("0b", "").zfill(36)
    n = []
    for a, m in zip(addr, mask):
        if m in ("X", "1"):
            n.append(m)
        else:
            n.append(a)
    n = "".join(n)
    out = []
    for comb in product([0, 1], repeat=n.count("X")):
        o = list(n)
        for c in comb:
            o[o.index("X")] = str(c)
        out.append(int("".join(o), 2))
    return out


def solve_pt2(data):
    memory = defaultdict(int)
    lines = data.splitlines()
    for line in lines:
        if line.startswith("mask"):
            mask = line.split(" ")[-1]
        else:
            addr, value = [int(f) for f in re.findall("\d+", line)]
            out = decode_mask(mask, addr)
            for o in out:
                memory[o] = value
    return sum(memory.values())


if __name__ == "__main__":
    data = get_data(year=2020, day=14)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_pt1(data)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")
