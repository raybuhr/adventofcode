from aocd import get_data
import pytest
from collections import defaultdict
from intcode import Intcode


def turn_and_step(direction, turn, position):
    if direction == "^":
        if turn == 0:  # turn left
            position = (position[0] - 1, position[1])
            direction = "<"
        elif turn == 1:  # turn right
            position = (position[0] + 1, position[1])
            direction = ">"
    elif direction == "v":
        if turn == 0:  # turn left
            position = (position[0] + 1, position[1])
            direction = ">"
        elif turn == 1:  # turn right
            position = (position[0] - 1, position[1])
            direction = "<"
    elif direction == ">":
        if turn == 0:  # turn left
            position = (position[0], position[1] + 1)
            direction = "^"
        elif turn == 1:  # turn right
            position = (position[0], position[1] - 1)
            direction = "v"
    elif direction == "<":
        if turn == 0:  # turn left
            position = (position[0], position[1] - 1)
            direction = "v"
        elif turn == 1:  # turn right
            position = (position[0], position[1] + 1)
            direction = "^"
    return position, direction


def paint(data, input_queue):
    hull = defaultdict(int)
    position = (0, 0)
    direction = "^"
    outputs = 0
    ic = Intcode(data, input_queue=input_queue)
    while True:
        try:
            op_code = ic.parse_op_code(ic.data[ic.position])
            ic.step()
            if op_code[0] == 4:
                outputs += 1
                if outputs % 2 == 0:
                    hull[position] = ic.output_queue.pop(0)
                    turn = ic.output_queue.pop(0)
                    position, direction = turn_and_step(direction, turn, position)
                    ic.input_queue.append(hull[position])
        except Intcode.Halt:
            break
    return hull


def print_message(hull):
    width = 1 + abs(min(h[0] for h in hull)) + abs(max(h[0] for h in hull))
    height = 1 + abs(min(h[1] for h in hull)) + abs(max(h[1] for h in hull))
    grid = [list("." * width) for _ in range(height)]
    for h, c in hull.items():
        x, y = h
        y = abs(y)
        if c == 1:
            grid[y][x] = "#"
    for g in grid:
        print("".join(g))


if __name__ == "__main__":
    data = get_data(year=2019, day=11)
    print("-" * 20, "Part 1:", "-" * 20)
    print(len(paint(data, [0])), "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    hull = paint(data, [1])
    print_message(hull)
