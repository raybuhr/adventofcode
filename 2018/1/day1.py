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
frequencies_seen = [0]

for change in changes:
    frequency = update_frequency(change, frequency)
    if frequency_map.get(frequency) is None:
        frequency_map[frequency] = 1
    else:
        frequency_map[frequency] += 1
    if frequency_map[frequency] == 2 and not_found_repeat_frequency:
        print(frequency)
        not_found_repeat_frequency = False

print('Part One:', frequency)

while not_found_repeat_frequency:
    for change in cycle(changes):
        frequency = update_frequency(change, frequency)
        if frequency_map.get(frequency) is None:
            frequency_map[frequency] = 1
        else:
            frequency_map[frequency] += 1
        if frequency_map[frequency] == 2 and not_found_repeat_frequency:
            print('Part Two:', frequency)
            not_found_repeat_frequency = False
            break