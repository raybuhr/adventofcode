#/usr/bin/env python3

from itertools import cycle

with open('input.txt') as stream:
    changes = stream.readlines()

def update_frequency(change: str, current_frequency: int) -> int:
    if change[0] == '+':
        current_frequency += int(change[1:])
    if change[0] == '-':
        current_frequency -= int(change[1:])
    return current_frequency

frequency = 0
frequency_map = {frequency: 1}
not_found_repeat_frequency = True

while not_found_repeat_frequency:
    len_input = len(changes)
    iterations = 0
    for change in cycle(changes):
        frequency = update_frequency(change, frequency)
        iterations += 1
        if frequency_map.get(frequency) is None:
            frequency_map[frequency] = 1
        else:
            frequency_map[frequency] += 1
        if iterations == len_input:
            print('Part One:', frequency)
        if frequency_map[frequency] == 2 and not_found_repeat_frequency:
            print('Part Two:', frequency)
            not_found_repeat_frequency = False
            break

print('Iterations:', iterations)