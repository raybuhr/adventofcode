#!/usr/bin/env python

import os

pwd = os.path.abspath(os.curdir)
filename = pwd + "/day4.txt"
print(filename)

with open(filename) as f:
    lines = f.readlines()

line_lengths = [len(x.strip("\n")) for x in lines]
uniq_lengths = [len(x.strip("\n")) for x in set(lines)]
valid_passwords = [1 for x in range(len(line_lengths)) if line_lengths[x] == uniq_lengths[x]]
print(sum(valid_passwords))
