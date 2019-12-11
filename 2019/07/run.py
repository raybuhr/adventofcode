from aocd import get_data
import itertools
from intcode import Intcode


def run(data, input_queue, verbose=False):
    intcode = Intcode(data=data, input_queue=input_queue)
    while True:
        try:
            intcode.step(verbose=verbose)
        except:
            break
    return intcode


def build_queue_from_phase_settings(phase_settings):
    queues = [[i] for i in phase_settings] + [[]]
    queues[0] += [0]
    return queues


def run_amplifier_circuit(data, queues):
    intcodes = {}
    for i in range(5):
        intcodes[i] = run(data, input_queue=queues[i])
        queues[i + 1] += intcodes[i].output_queue
    return queues


def test_run_amplifier_circuit_1():
    test_data = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
    test_phases = [4, 3, 2, 1, 0]
    expect = [43210]
    queues = build_queue_from_phase_settings(test_phases)
    got = run_amplifier_circuit(test_data, queues)
    assert expect == got[-1]


def test_run_amplifier_circuit_2():
    test_data = (
        "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
    )
    test_phases = [0, 1, 2, 3, 4]
    expect = [54321]
    queues = build_queue_from_phase_settings(test_phases)
    got = run_amplifier_circuit(test_data, queues)
    assert expect == got[-1]


def test_run_amplifier_circuit_3():
    test_data = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
    test_phases = [1, 0, 4, 3, 2]
    expect = [65210]
    queues = build_queue_from_phase_settings(test_phases)
    got = run_amplifier_circuit(test_data, queues)
    assert expect == got[-1]


def solve_part1(data):
    best = 0
    for p in itertools.permutations(range(5)):
        queues = build_queue_from_phase_settings(p)
        run_amplifier_circuit(data, queues)
        output = queues[-1]
        if output[0] > best:
            best = output[0]
    return best


def run_amplifier_loop(data, phase_settings, num_times=1):
    start = build_queue_from_phase_settings(phase_settings)
    queues = build_queue_from_phase_settings(phase_settings)

    def run_loop(data, queues):
        run_amplifier_circuit(data, queues)
        queues = queues[::-1]
        return [start[i] + queues[i] for i in range(len(start))]

    best = 0
    done = False
    while not done:
        queues = run_loop(data, queues)
        new_best = queues[0][-1]
        if new_best > best:
            best = new_best
        else:
            done = True
    return best


def test_run_amplifier_loop_1():
    test_data = "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,\
    27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
    test_phases = [9, 8, 7, 6, 5]
    got = run_amplifier_loop(test_data, test_phases)
    assert got == 139629729


def test_run_amplifier_loop_2():
    test_data = "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,\
    -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,\
    53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
    test_phases = [9, 7, 8, 5, 6]
    got = run_amplifier_loop(test_data, test_phases)
    assert got == 18216


def solve_part2(data):
    best = 0
    for p in itertools.permutations(range(5, 10)):
        output = run_amplifier_loop(data, p)
        if output > best:
            best = output
    return best


if __name__ == "__main__":
    data = get_data(year=2019, day=7)
    print("-" * 20, "Part 1:", "-" * 20)
    print(solve_part1(data), "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    print(solve_part2(data), "\n")
