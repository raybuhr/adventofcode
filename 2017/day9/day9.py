#!/usr/bin/env python

with open("day9.txt") as f:
    lines = f.readlines()

stream = lines[0].strip("\n")

def remove_cancel(text):
    garbage_idx = []
    for idx, val in enumerate(text):
        if val == "!":
            garbage_idx.append(idx)
            garbage_idx.append(idx+1)
    keep_ids = [x for x in range(len(text)) if x not in garbage_idx]
    keep_vals = [text[x] for x in keep_ids]
    new_data = ''.join(keep_vals)
    return new_data


def remove_garbage(text):
    new_data = [x for x in text]
    return new_data

print(len(stream))
print(len(remove_cancel(stream)))
print(remove_cancel(stream))
