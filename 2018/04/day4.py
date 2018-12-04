#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict, Counter
import re

with open('input.txt') as file:
    event = sorted(file.read().split('\n'))

guards = defaultdict(Counter)


def find_guard(string):
    match = re.search(string=string, pattern='Guard #\d+')
    if match is None:
        return None
    return match.group(0)


for e in event:
    minute, status = e.split(']')
    # parse minute
    m = int(minute[-2:])
    # set guard the first time seen and leave until change
    if "Guard #" in status:
        guard = find_guard(status)
    if 'asleep' in status:
        start = m
    if 'wakes' in status:
        mins_asleep = m - start
        guards[guard].update(Counter(start + i for i in range(mins_asleep)))


def total_time_asleep(guard):
    return sum(guards[guard].values())


def guard_id(guard):
    return int(guard.split('#')[1])


def most_sleepy_minute(guard):
    return guards[guard].most_common()[0]


current_max = 0
sleepy_guard = ''
for guard in guards:
    time_asleep = total_time_asleep(guard)
    if time_asleep > current_max:
        current_max = time_asleep
        sleepy_guard = guard


sleepy_minute = most_sleepy_minute(sleepy_guard)[0]

print('Part One:', sleepy_minute * guard_id(sleepy_guard))

current_max = 0
common_napper = ''
for guard in guards:
    sleepy_min = most_sleepy_minute(guard)
    if sleepy_min[1] > current_max:
        common_napper = guard
        current_max = sleepy_min[1]
        max_minute = sleepy_min[0]


print('Part Two:', guard_id(common_napper) * max_minute)
