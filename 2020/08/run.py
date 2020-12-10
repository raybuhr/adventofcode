from aocd import get_data
from handholdconsole import HandHoldGameConsole


def solve_pt1(data):
    console = HandHoldGameConsole(data)
    console.parse_data()
    console.run()
    return console.accumulator


def solve_pt2(data):
    console = HandHoldGameConsole(data)
    console.parse_data()
    jumps = console.run(log_jump_locs=True)
    for j in jumps:
        console = HandHoldGameConsole(data)
        console.replace_instructions(position=j)
        console.run()


if __name__ == "__main__":
    data = get_data(year=2020, day=8)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_pt1(data)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")
