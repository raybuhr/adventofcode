from aocd import get_data
import pytest
from intcode import Intcode


def boot_network(data):
    network = {}
    for i in range(50):
        network[i] = Intcode(data, input_queue=[i])
    return network


def step_network(network, verbose=False):
    for i, ic in network.items():
        if i > 50:
            continue
        if len(ic.input_queue) == 0:
            ic.input_queue.append(-1)
        ic.run()
        if len(ic.output_queue) > 0:
            address = ic.output_queue.pop(0)
            x = ic.output_queue.pop(0)
            y = ic.output_queue.pop(0)
            if address == 255:
                if verbose:
                    print(y)
                network[address] = [x, y]
            else:
                network[address].input_queue.extend([x, y])


def solve_part1(data):
    network = boot_network(data)
    while True:
        try:
            step_network(network, True)
        except RuntimeError:
            break


def solve_part2(data):
    network = boot_network(data)
    network[255] = None
    last_y = None
    # run once to initialize
    step_network(network)
    idle_counter = 0
    while True:
        step_network(network)
        idle = all(len(v.input_queue) == 0 for k, v in network.items() if k < 50)
        if idle:
            idle_counter += 1
        if idle_counter > 2:
            x, y = network[255]
            if y == last_y:
                print(y)
                break
            else:
                last_y = y
            network[0].input_queue.extend([x, y])
            idle_counter = 0


if __name__ == "__main__":
    data = get_data(year=2019, day=23)

    print("-" * 20, "Part 1:", "-" * 20)
    solve_part1(data)

    print("-" * 20, "Part 2:", "-" * 20)
    solve_part2(data)
