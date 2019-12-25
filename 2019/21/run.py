from aocd import get_data
from intcode import Intcode


def string_to_ascii_list(string):
    return [ord(x) for x in list(string)]


def ascii_list_to_string(ascii_list):
    output = []
    for x in ascii_list:
        try:
            o = chr(x)
            output.append(o)
        except ValueError:
            o = ""
            output.append(o)
    return "".join(output)


def run_program(data, instructions):
    ic = Intcode(data, input_queue=[])
    ic.run()
    for inst in instructions:
        ic.input_queue.extend(string_to_ascii_list(inst))
        ic.run()
    print(ascii_list_to_string(ic.output_queue))
    return ic.output_queue[-1]


def solve_part1(data):
    instructions = [
        "NOT A T\n",
        "NOT B J\n",
        "OR T J\n",
        "NOT C T\n",
        "OR T J\n",
        "AND D J\n",
        "WALK\n",
    ]
    return run_program(data, instructions)


def solve_part2(data):
    instructions = [
        "NOT A T\n",
        "NOT B J\n",
        "OR T J\n",
        "NOT C T\n",
        "OR T J\n",
        "AND D J\n",
        "NOT E T\n",
        "NOT T T\n",
        "OR H T\n",
        "AND T J\n",
        "RUN\n",
    ]
    return run_program(data, instructions)


if __name__ == "__main__":
    data = get_data(year=2019, day=21)

    print("-" * 20, "Part 1:", "-" * 20)
    print(solve_part1(data), "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    print(solve_part2(data), "\n")
