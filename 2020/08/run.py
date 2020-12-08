from aocd import get_data
from copy import deepcopy

def parse_data(data):
    return [d.split() for d in data.splitlines()]


def step(pos, acc, instructions):
    inst, val = instructions[pos]
    val = int(val)
    if inst == "acc":
        acc += val
        pos += 1
    elif inst == "jmp":
        pos += val
    elif inst == "nop":
        pos += 1
    return pos, acc


def run(instructions, log_jump_locs=False):
    pos, acc, seen= 0, 0, []
    if log_jump_locs:
        jump_locs = []
    while pos not in seen:
        seen += [pos]
        try:
            pos, acc = step(pos, acc, instructions)
            if log_jump_locs and "jmp" in instructions[pos]:
                jump_locs += [pos]
        except IndexError:
            print(acc)
            break
    if log_jump_locs:
        return acc, jump_locs
    return acc


def replace_instructions(pos, instructions):
    inst = deepcopy(instructions)
    inst[pos][0] = 'nop'
    return inst


def solve_pt1(data):
    instructions = parse_data(data)
    return run(instructions)


def solve_pt2(data):
    instructions = parse_data(data)
    _, jumps = run(instructions, True)
    for j in jumps:
        run(replace_instructions(j, instructions))
    return ":-)"


if __name__ == "__main__":
    data = get_data(year=2020, day=8)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_pt1(data)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")
