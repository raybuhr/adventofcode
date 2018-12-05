#!/usr/bin/env python
# coding: utf-8

with open('data.txt') as raw_data:
    data = raw_data.read()

test_string = 'dabAcCaCBAcCcaDA'
test_pass = 'dabCBAcaDA'


def remove_negating_units(text):
    inital_len = len(text)
    for c in set(text):
        text = text.replace(c.upper() + c.lower(), '').replace(c.lower() + c.upper(), '')
    return inital_len != len(text), text


def reduce_polymer(text):
    while True:
        changed, text = remove_negating_units(text)
        if not changed:
            break
    return text


print('Part one:', len(reduce_polymer(data)))


def reduce_polymer_max(text):
    units = set(text.lower())
    poly_count = {}
    for c in units:
        new_data = text.replace(c, '').replace(c.upper(), '')
        poly_count[c] = reduce_polymer(new_data)
    poly_lens = [len(v) for v in poly_count.values()]
    best_poly = [v for v in poly_count.values() if len(v) == min(poly_lens)]
    return best_poly[0]

print('Part Two:', len(reduce_polymer_max(data)))
