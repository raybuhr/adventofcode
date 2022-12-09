from collections import defaultdict

with open("input.txt") as f:
    steps = [line.split() for line in f.read().splitlines()]


def move_head(direction, head):
    if direction == "R":
        head[0] += 1
    elif direction == "L":
        head[0] -= 1
    elif direction == "U":
        head[1] += 1
    elif direction == "D":
        head[1] -= 1


def is_tail_close(head, tail):
    x = abs(head[0] - tail[0])
    y = abs(head[1] - tail[1])
    return x < 2 and y < 2


def move_tail(head, tail):
    if not is_tail_close(head, tail):
        x = head[0] - tail[0]
        y = head[1] - tail[1]
        if abs(x) > 0 and abs(y) > 0:
            # move diagonal
            tail[0] += x / abs(x)
            tail[1] += y / abs(y)
        else:
            if abs(x) > abs(y):
                tail[0] += x / abs(x)
            else:
                tail[1] += y / abs(y)


def part_a(steps):
    seen = defaultdict(int)
    head = [0, 0]
    tail = [0, 0]
    seen[tuple(tail)] += 1
    for direction, amount in steps:
        amount = int(amount)
        while amount > 0:
            amount -= 1
            move_head(direction, head)
            move_tail(head, tail)
            seen[tuple(tail)] += 1
    return len(seen)


print("part a:", part_a(steps))


def part_b(steps):
    seen = defaultdict(int)
    head = [0, 0]
    t1 = [0, 0]
    t2 = [0, 0]
    t3 = [0, 0]
    t4 = [0, 0]
    t5 = [0, 0]
    t6 = [0, 0]
    t7 = [0, 0]
    t8 = [0, 0]
    t9 = [0, 0]
    seen[tuple(t9)] += 1
    for direction, amount in steps:
        amount = int(amount)
        while amount > 0:
            amount -= 1
            move_head(direction, head)
            move_tail(head, t1)
            move_tail(t1, t2)
            move_tail(t2, t3)
            move_tail(t3, t4)
            move_tail(t4, t5)
            move_tail(t5, t6)
            move_tail(t6, t7)
            move_tail(t7, t8)
            move_tail(t8, t9)
            seen[tuple(t9)] += 1
    return len(seen)


print("part b:", part_b(steps))
