#!/usr/bin/env python
# coding: utf-8

with open('data.txt') as f:
    data = f.read().split()
    data = [int(d) for d in data]

test_data = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
test_data = test_data.split()
test_data = [int(d) for d in test_data]


def process_data(data):
    nodes = data[0]
    num_metadata = data[1]
    data = data[2:]
    metadata_total = 0
    
    for i in range(nodes):
        metadata, data = process_data(data)
        metadata_total += metadata
    
    metadata_total += sum(data[:num_metadata])
    
    if nodes == 0:
        return metadata_total, data[num_metadata:]
    else:
        return metadata_total, data[num_metadata:]


assert process_data(test_data) == (138, [])
print('Part One:', process_data(data)[0])


def score_root_node(data, debug=False):
    nodes = data[0]
    num_metadata = data[1]
    data = data[2:]
    node_values = []
    
    for i in range(nodes):
        node_vals, data = score_root_node(data)
        node_values.append(node_vals)
        
    def _keep_node_values(node_values, data, num_metadata):
        vals = []
        for meta in data[:num_metadata]:
            if meta > 0 and meta <= len(node_values):
                vals.append(node_values[meta - 1])
        return vals
    
    if nodes == 0:
        node_val = sum(data[:num_metadata])
        new_data = data[num_metadata:]
        return node_val, new_data
    else:
        kept_node_values = _keep_node_values(node_values, data, num_metadata)
        if debug:
            print('node_values:', node_values, '<|> ', data, ', pick', num_metadata, ', kept:', kept_node_values)
        return sum(kept_node_values), data[num_metadata:]


assert score_root_node(test_data) == (66, [])
print('Part Two:', score_root_node(data)[0])
