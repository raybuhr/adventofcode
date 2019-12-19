from aocd import get_data
from collections import defaultdict
import random
import pytest
from intcode import Intcode


NORTH = 1
SOUTH = 2
WEST = 3 
EAST= 4
WALL = 0
OK = 1
STOP = 2


def get_next_position(direction, x, y):
    if direction == NORTH:
        return x, y+1
    elif direction == SOUTH:
        return x, y-1
    elif direction == WEST:
        return x-1, y
    elif direction == EAST:
        return x+1, y


def turn(direction):
    if direction == NORTH:
        return EAST
    elif direction == SOUTH:
        return WEST
    elif direction == EAST:
        return SOUTH
    elif direction == WEST:
        return NORTH


def turn_random(direction):
    while True:
        d = random.choice(range(1, 5))
        if d != direction:
            return d


def run(data, limit=float('inf'), debug=False, print_steps=10):
    counter = 0
    positions = defaultdict(int)
    x, y = 0, 0
    direction = WEST
    turns = 0
    path = []
    ic = Intcode(data, input_queue=[direction])
    while counter < limit:
        ic.run()
        result = ic.output_queue.pop()
        if result == OK:
            positions[(x,y)] = "-"
            x, y = get_next_position(direction, x, y)
            path.append((x,y))
        elif result == WALL:
            positions[get_next_position(direction, x, y)] = "#"
            direction = turn_random(direction)
            # turns += 1
            # # turn again if find going in a circle
            # if turns % 4 == 0:
            #     direction = turn_random(direction)
            x, y = get_next_position(direction, x, y)
            path.append((x,y))
        elif result == STOP:
            positions[(x,y)] = "-"
            x, y = get_next_position(direction, x, y)
            path.append((x,y))
            positions[(x,y)] = "$"
            print("$$$$")
            return positions
        ic.input_queue.append(direction)
        counter += 1
        if counter % print_steps == 0 and debug:
            print("After", counter, "Steps")
            print_map(positions)
            print(" ")
    return positions, counter, path


def print_map(positions):
    min_x = min(k[0] for k in positions)
    max_x = max(k[0] for k in positions)
    min_y = min(k[1] for k in positions)
    max_y = max(k[1] for k in positions)
    width = range(min_x, max_x + 1)
    height = range(min_y, max_y + 1)
    board = [[" " for _ in width] for _ in height]
    for k, v in positions.items():
        x = abs(min_x) + k[0]
        y = abs(min_y) + k[1]
        board[y][x] = v
    for row in board[::-1]: # print mirror image
        print(row)



def solve_part1():
    pass


def solve_part2():
    pass


if __name__ == "__main__":
    data = get_data(year=2019, day=15)
    print("-" * 20, "Part 1:", "-" * 20)
    print(solve_part1(), "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    print(solve_part2())
