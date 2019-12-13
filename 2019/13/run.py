from aocd import get_data
import pytest
from intcode import Intcode


def parse_instructions(instructions):
    x = instructions.pop(0)
    y = instructions.pop(0)
    tile = instructions.pop(0)
    return (x, y, tile)


def run_program(data, input_queue):
    tiles = []
    ic = Intcode(data, input_queue=input_queue)
    while True:
        try:
            while len(ic.output_queue) < 3:
                ic.step()
            tile = parse_instructions(ic.output_queue)
            tiles.append(tile)
        except:
            break
    return tiles


def solve_part1(data):
    tiles = run_program(data, [])
    return len([z for x, y, z in tiles if z == 2])


def make_game_free(data):
    free = [i for i in data.split(',')]
    free[0] = '2'
    return ','.join(free)


def setup_game(data):
    game = make_game_free(data)
    ic = Intcode(game, [])
    ic.board = {}
    ic.ball_position, ic.paddle_position = None, None
    return ic


def run_game(ic):
    ic.run()
    while len(ic.output_queue) > 0:
        x,y,z = parse_instructions(ic.output_queue)
        ic.board[(x,y)] = z
        if z == 3:
            ic.paddle_position = x
        if z == 4:
            ic.ball_position = x
    if ic.ball_position > ic.paddle_position:
        ic.input_queue.append(1)
    elif ic.ball_position < ic.paddle_position:
        ic.input_queue.append(-1)
    else:
        ic.input_queue.append(0)
    return ic


def count_blocks(board):
    return sum(v == 2 for v in board.values())


def solve_part2(data):
    ic = setup_game(data)
    run_game(ic)
    blocks = count_blocks(ic.board)
    while blocks > 0:
        run_game(ic)
        blocks = count_blocks(ic.board)
    return ic


if __name__ == "__main__":
    data = get_data(year=2019, day=13)
    print("-" * 20, "Part 1:", "-" * 20)
    print(solve_part1(data), "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    ic = solve_part2(data)
    print(ic.board[(-1,0)])
