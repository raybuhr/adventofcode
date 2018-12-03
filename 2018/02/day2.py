#!/usr/bin/env python
# coding: utf-8

with open('input.txt') as file:
    data = [d.strip('\n') for d in file.readlines()]

letters = 'abcdefghijklmnopqrstuvwxyz'

freq = {}
for l in letters:
    freq[l] = 0


def data_line_freq(line):
    counter = freq.copy()
    for l in line:
        counter[l] += 1
    return counter


freqs = [data_line_freq(x) for x in data]
twos = [2 in x.values() for x in freqs]
threes = [3 in x.values() for x in freqs]

print('Part 1:', sum(twos) * sum(threes))


def diff_chars(str1, str2):
    diff = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff += 1
    return diff


assert diff_chars('fghij', 'fguij') == 1
assert diff_chars('abcde', 'axcye') == 2

close_lines = set()
for line in data:
    for other_line in data:
        if line != other_line:
            if diff_chars(line, other_line) == 1:
                close_lines.add(line)
                close_lines.add(other_line)

close_lines = list(close_lines)
same_chars = ''
for i in range(len(close_lines[0])):
    if close_lines[0][i] == close_lines[1][i]:
        same_chars += close_lines[0][i]

print('Part Two:', same_chars)
