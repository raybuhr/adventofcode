from aocd import get_data
import pytest


def form_pattern(position, length):
    base_pattern = [i for i in [0, 1, 0, -1] for _ in range(position)]
    repetitions = length // len(base_pattern) + 1
    pattern = base_pattern * repetitions
    return pattern[1 : length + 1]


def fft(data):
    signal = [int(i) for i in data]
    length = len(signal)
    output = [
        sum(sg * p for sg, p in zip(signal, form_pattern(i, length)))
        for i in range(1, length + 1)
    ]
    return "".join([str(o)[-1] for o in output])


def run_fft(data, phases):
    for _ in range(phases):
        data = fft(data)
    return data


def part2(data, phases):
    signal = [int(i) for i in data]
    offset = int("".join(map(str, signal[:7])))
    signal = signal * 10000
    for p in range(phases):
        for i in range(len(signal) - 2, offset - 1, -1):
            signal[i] = (signal[i] + signal[i + 1]) % 10
    return "".join([str(o) for o in signal[offset : offset + 8]])


test_cases = [
    ("12345678", 4, "01029498"),
    ("80871224585914546619083218645595", 100, "24176176"),
    ("19617804207202209144916044189917", 100, "73745418"),
    ("69317163492948606335995924319873", 100, "52432133"),
]


@pytest.mark.parametrize("input_signal,phases,expected", test_cases)
def test_run_fft(input_signal, phases, expected):
    ouput = run_fft(input_signal, phases)
    assert ouput[:8] == expected


more_test_cases = [
    ("03036732577212944063491565474664", 100, "84462026"),
    ("02935109699940807407585447034323", 100, "78725270"),
    ("03081770884921959731165446850517", 100, "53553731"),
]


@pytest.mark.parametrize("input_signal,phases,expected", more_test_cases)
def test_part2(input_signal, phases, expected):
    assert part2(input_signal, phases) == expected


if __name__ == "__main__":
    data = get_data(year=2019, day=16)

    print("-" * 20, "Part 1:", "-" * 20)
    output = run_fft(data, 100)
    print(output[:8], "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    print(part2(data, 100), "\n")
