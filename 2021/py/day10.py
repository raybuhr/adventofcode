import statistics
import sys


points = {")": 3, "]": 57, "}": 1197, ">": 25137}
closes = {")": "(", "]": "[", "}": "{", ">": "<"}
opens = {v: k for k, v in closes.items()}


def parse_data(filename):
    with open(filename) as f:
        data = f.read().splitlines()
    return data


def check_line(line):
    left = []
    ct = 0
    for char in line:
        if char in opens:
            left.append(char)
            ct += 1
        elif char in closes:
            if closes[char] == left.pop():
                ct += 1
                continue
            else:
                return points[char]
    return 0


def part_one(data):
    total = 0
    for l in data:
        pts = check_line(l)
        total += pts
    return total


def complete_line(line):
    left = []
    ct = 0
    for char in line:
        if char in opens:
            left.append(char)
            ct += 1
        elif char in closes:
            if closes[char] == left.pop():
                ct += 1
                continue
            else:
                return 0
    right = []
    while left:
        right.append(opens[left.pop()])
    score_map = {")": 1, "]": 2, "}": 3, ">": 4}
    score = 0
    for r in right:
        score *= 5
        score += score_map[r]
    return score


def part_two(data):
    scores = []
    for l in data:
        s = complete_line(l)
        if s > 0:
            scores.append(s)
    return statistics.median(scores)


if __name__ == "__main__":
    filename = sys.argv[1]
    data = parse_data(filename)
    print("Part One")
    print(part_one(data))
    print("Part Two")
    print(part_two(data))
