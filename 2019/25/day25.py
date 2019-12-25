from aocd import get_data
import pytest
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


def run(data):
    ic = Intcode(data, input_queue=[])
    while True:
        try:
            ic.run()
            print(ascii_list_to_string(ic.output_queue))
            ic.output_queue.clear()
            cmd = input("Command: ")
            if cmd == "exit" or cmd == "q":
                break
            if cmd == "help":
                print("space heater, semiconductor, hypercube, festive hat")
            ic.input_queue.extend(string_to_ascii_list(cmd + "\n"))
        except:
            break


if __name__ == "__main__":
    data = get_data(year=2019, day=25)

    print("-" * 20, "Part 1:", "-" * 20)
    run(data)

    print("-" * 20, "Part 2:", "-" * 20)
