from aocd import get_data
from intcode import Intcode


def run(data, input_queue, verbose=False):
    intcode = Intcode(data=data, input_queue=input_queue)
    while True:
        try:
            intcode.step(verbose=verbose)
        except:
            break
    return intcode


def solve_part1(data, ins):
    intcode = run(data, ins)
    return intcode.output_queue


def test_solve_part1():
    case1 = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    expect1 = list(Intcode.parse_data(case1).values())
    got1 = solve_part1(case1, [])
    assert expect1 == got1
    case2 = "1102,34915192,34915192,7,4,7,99,0"
    got2 = solve_part1(case2, [])
    got2_len = len(str(got2[0]))
    assert got2_len == 16
    case3 = "104,1125899906842624,99"
    expect3 = Intcode.parse_data(case3)[1]
    got3 = solve_part1(case3, [])
    assert expect3 == got3[0]


if __name__ == "__main__":
    data = get_data(year=2019, day=9)
    print("-" * 20, "Part 1:", "-" * 20)
    print(solve_part1(data, [1]), "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    print(solve_part1(data, [2]), "\n")
