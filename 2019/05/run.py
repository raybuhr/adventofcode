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


def solve(data, input_queue):
    intcode = run(data, input_queue)
    return intcode.output_queue[-1]


if __name__ == "__main__":
    data = get_data(year=2019, day=5)
    print("-" * 10 + "Part 1: " + "-" * 10)
    print(solve(data, [1]))
    print("\n" + "-" * 10 + "Part 2: " + "-" * 10)
    print(solve(data, [5]))
