import json

def read_packets(filename):
    with open(filename) as f:
        pairs = f.read().strip().split("\n\n")
        packets = []
        for pair in pairs:
            a, b = pair.split("\n")
            packets.append([json.loads(a), json.loads(b)])
        return packets


def compare(a, b, idx=0):
    try:
        a_ = a[idx]
    except IndexError:
        return True
    try:
        b_ = b[idx]
    except IndexError:
        return False
    if isinstance(a_, int) and isinstance(b_, int):
        if a > b:
            return False
        idx += 1
    elif isinstance(a_, int) and isinstance(b_, list):
        a_ = [a_]
        return compare(a_, b_)
    elif isinstance(a_, list) and isinstance(b_, int):
        b_ = [b_]
        return compare(a_, b_)
    elif isinstance(a_, list) and isinstance(b_, list):
        if a_ == [] and b_ != []:
            return True
        elif a_ != [] and b_ == []:
            return False
        elif a_ == [] and b_ == []:
            idx += 1
            return compare(a, b, idx)
        return compare(a_, b_)
    return True


def sum_compared_indexes(packets):
    val = 0
    for i, pair in enumerate(packets, 1):
        a, b = pair
        if compare(a, b):
            val += i
    return val


packets = read_packets("input.txt")

# TODO - bugs on 46, 149
print(
    compare(packets[46][0], packets[46][1])
)
