from collections import defaultdict

with open("input.txt") as f:
    lines = f.read().splitlines()


def make_queue(lines):
    queue = defaultdict(int)
    c = 1

    for line in lines:
        if line.startswith("addx"):
            v = int(line.replace("addx ", ""))
            c += 2
            queue[c] += v
        else:
            c += 1

    return queue


def run(lines, cycles=220):
    queue = make_queue(lines)
    X = 1
    signals = []

    for i in range(1, cycles + 1):
        X += queue[i]
        if i in range(20, cycles + 1, 40):
            signals.append(X * i)

    return sum(signals)


def draw(lines, cycles=240):
    queue = make_queue(lines)
    X = 1
    message = ""
    sprite = 1

    for i in range(1, cycles + 1):
        X += queue[i]
        if (i - 1) % 40 - X in (-1, 0, 1):
            message += "X"
        else:
            message += " "

    message = [message[i : i + 40] for i in range(0, cycles + 1, 40)]
    return message


print("part a:", run(lines))

print("part b:")
for line in draw(lines):
    print(line)
