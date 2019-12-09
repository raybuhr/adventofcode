from aocd.models import Puzzle
from collections import defaultdict
import itertools


def get_data():
    puzzle = Puzzle(year=2019, day=9)
    data = puzzle.input_data
    return data


def parse_data(data):
    dd = defaultdict(int)
    d = [int(d) for d in data.split(",")]
    for i, v in enumerate(d):
        dd[i] = v
    return dd


def parse_op_code(op_code):
    op = str(op_code)
    if len(op) < 5:
        op = op.rjust(5, "0")
    code = int(op[3:])
    third, second, first = int(op[0]), int(op[1]), int(op[2])
    return (code, first, second, third)


def run_intcode(data, input_values, output_queue,
        position=0, relative_base=0, verbose=False):
    done = False
    while not done:
        instructions = parse_op_code(data[position])
        op, mode1, mode2, mode3 = instructions
        params = [data[position + i] for i in range(1, 4)]
        if verbose:
            print("-----Step-----")
            print("opcode", op)
            print("modes", instructions[1:])
            print("params", params[:3])
            print("position", position)
            print("relative_base", relative_base)
        if op == 99:
            done = True
        elif op == 1:
            out = params[2]
            if mode3 == 2:
                out += relative_base
            if mode1 == 0:
                in1 = data[params[0]]
            if mode1 == 1:
                in1 = params[0]
            if mode1 == 2:
                in2 = data[params[0] + relative_base]
            if mode2 == 0:
                in2 = data[params[1]]
            if mode2 == 1:
                in2 = params[1]
            if mode2 == 2:
                in2 = data[params[1] + relative_base]
            data[out] = in1 + in2
            position += 4
        elif op == 2:
            out = params[2]
            if mode3 == 2:
                out += relative_base
            if mode1 == 0:
                in1 = data[params[0]]
            if mode1 == 1:
                in1 = params[0]
            if mode1 == 2:
                in1 = data[params[0] + relative_base]
            if mode2 == 0:
                in2 = data[params[1]]
            if mode2 == 1:
                in2 = params[1]
            if mode2 == 2:
                in2 = data[params[1] + relative_base]
            data[out] = in1 * in2
            position += 4
        elif op == 3:
            if mode1 == 0:
                out = data[params[0]]
            if mode1 == 1:
                out = params[0]
            if mode1 == 2:
                out = data[params[0]] + relative_base
            try:
                print(instructions)
                print("mode", mode1)
                print("base", relative_base)
                print("out", out)
                print("current value", data[out])
                print(input_values)
                new_val = input_values.pop(0)
                data[out] = new_val
                print("new value", data[out])
                position += 2
            except:
                done = True
        elif op == 4:
            if mode1 == 0:
                out = data[params[0]]
            if mode1 == 1:
                out = params[0]
            if mode1 == 2:
                out = data[params[0] + relative_base]
            output_queue.append(out)
            position += 2
        elif op == 5:  # jump-if-true
            if mode1 == 0:
                first = data[params[0]]
            if mode1 == 1:
                first = params[0]
            if mode1 == 2:
                first = data[params[0] + relative_base]
            if mode2 == 0:
                second = data[params[1]]
            if mode2 == 1:
                second = params[1]
            if mode2 == 2:
                second = data[params[1] + relative_base]
            if first != 0:
                position = second
            else:
                position += 3
        elif op == 6:  # jump-if-false
            if mode1 == 0:
                first = data[params[0]]
            if mode1 == 1:
                first = params[0]
            if mode1 == 2:
                first = data[params[0] + relative_base]
            if mode2 == 0:
                second = data[params[1]]
            if mode2 == 1:
                second = params[1]
            if mode2 == 2:
                second = data[params[1] + relative_base]
            if first == 0:
                position = second
            else:
                position += 3
        elif op == 7:  # less than
            if mode1 == 0:
                first = data[params[0]]
            if mode1 == 1:
                first = params[0]
            if mode1 == 2:
                first = data[params[0] + relative_base]
            if mode2 == 0:
                second = data[params[1]]
            if mode2 == 1:
                second = params[1]
            if mode2 == 2:
                second = data[params[1] + relative_base]
            out = params[2]
            if mode3 == 2:
                out += relative_base
            if first < second:
                data[out] = 1
            else:
                data[out] = 0
            position += 4
        elif op == 8:  # equals
            if mode1 == 0:
                first = data[params[0]]
            if mode1 == 1:
                first = params[0]
            if mode1 == 2:
                first = data[params[0] + relative_base]
            if mode2 == 0:
                second = data[params[1]]
            if mode2 == 1:
                second = params[1]
            if mode2 == 2:
                second = data[params[1] + relative_base]
            out = params[2]
            if mode3 == 2:
                out += relative_base
            if first == second:
                data[out] = 1
            else:
                data[out] = 0
            position += 4
        elif op == 9:  # change relative base
            out = params[0]
            if mode1 == 2:
                out += relative_base
            relative_base += out
            position += 2
        else:
            raise ValueError(
                "Unknown op_code",
                data[position],
                position,
                op,
                mode1,
                mode2,
                mode3,
                params,
            )
    return data, output_queue


def solve_part1(data, ins, outs):
    codes = parse_data(data)
    run_intcode(codes, ins, outs)
    return outs


def test_solve_part1():
    case1 = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    expect1 = list(parse_data(case1).values())
    got1 = solve_part1(case1, [], [])
    assert expect1 == got1
    case2 = "1102,34915192,34915192,7,4,7,99,0"
    got2 = solve_part1(case2, [], [])
    got2 = len(str(got2[0])) 
    assert got2 == 16
    case3 = "104,1125899906842624,99"
    expect3 = parse_data(case3)[1]
    got3 = solve_part1(case3, [], [])[0]
    assert expect3 == got3


def solve_part2(data):
    pass


if __name__ == "__main__":
    data = get_data()
    print("-"*20, "Part 1:", "-"*20)
    print(solve_part1(data, [1], []), "\n")

    print("-"*20, "Part 2:", "-"*20)
    solve_part2(data)

