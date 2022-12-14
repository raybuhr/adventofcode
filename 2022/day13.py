import json
from functools import cmp_to_key


def read_packets(filename):
    with open(filename) as f:
        pairs = f.read().strip().split("\n\n")
        packets = []
        for pair in pairs:
            a, b = pair.split("\n")
            packets.append([json.loads(a), json.loads(b)])
        return packets


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            return -1
        if b > a:
            return 1
        return 0
    else:
        if isinstance(a, int):
            a = [a]
        if isinstance(b, int):
            b = [b]
        if a == [] and b != []:
            return 1
        if a != [] and b == []:
            return -1
        if a == [] and b == []:
            return 0
        c = compare(a[0], b[0])
        if c:
            return c
        else:
            return compare(a[1:], b[1:])


def sum_compared_indexes(packets):
    val = 0
    for i, pair in enumerate(packets, 1):
        if compare(*pair) > 0:
            val += i
    return val


def sort_packets(packets):
    packets_ = []
    for a, b in packets:
        packets_.append(a)
        packets_.append(b)
    packets_.append([[2]])
    packets_.append([[6]])
    packets_ = sorted(packets_, key=cmp_to_key(compare), reverse=True)
    return packets_


packets = read_packets("input.txt")
sorted_packets = sort_packets(packets)

print("part a:", sum_compared_indexes(packets))
print("part b:", (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))
