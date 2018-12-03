#!/usr/bin/env python
# coding: utf-8

with open('input.txt') as file:
    data = [d.strip('\n') for d in file.readlines()]

data = {int(d[0].replace('#', '')): d[1] for d in [d.split(' @ ') for d in data]}


def value_from_left(instruction: str):
    d = instruction.split(',')
    return int(d[0])


def value_from_top(instruction: str):
    first_split = instruction.split(',')
    second_split = first_split[1].split(':')
    return int(second_split[0])


def small_square_size(instruction: str):
    first_split = instruction.split(': ')
    second_split = first_split[1].split('x')
    return int(second_split[0]), int(second_split[1])


def parse_instruction(instruction: str):
    small_square = small_square_size(instruction)
    return {
        'dist_from_left': value_from_left(instruction),
        'dist_from_top': value_from_top(instruction),
        'num_right': small_square[0],
        'num_down': small_square[1],
    }


def fabric_positions(dist_from_left: int, dist_from_top: int, num_right: int, num_down: int):
    '''Assumes top-left corner is (0, 0)'''
    positions = set()
    for x in range(dist_from_left, dist_from_left + num_right):
        for y in range(dist_from_top, dist_from_top + num_down):
            positions.add((x, -y))
    return positions


instructions = dict(zip(data.keys(), [parse_instruction(i) for i in data.values()]))

all_positions = {}
for k, v in instructions.items():
    all_positions[k] = fabric_positions(**v)

unique_positions = {}
for vals in all_positions.values():
    for pos in vals:
        if unique_positions.get(pos) is None:
            unique_positions[pos] = 1
        else:
            unique_positions[pos] += 1


print('Part One:', len([x for x in unique_positions.values() if x > 1]))


def claim_overlaps(claim):
    claim_pos = all_positions[claim]
    overlaps = []
    for k, v in all_positions.items():
        if k == claim:
            continue
        if bool(claim_pos & v):
            return True
    return False


print('Part Two:', [claim for claim in data if not claim_overlaps(claim)])
