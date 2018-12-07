#!/usr/bin/env python
# coding: utf-8

from string import ascii_lowercase

test_data = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.',
]

with open('data.txt') as f:
    data = f.read().split('\n')


def process_instruction(text: str):
    line = text.lower()
    steps = line.split('step ')
    return steps[1][0], steps[2][0]

test_steps = [process_instruction(text) for text in test_data]
steps = [process_instruction(text) for text in data]


def unique_nodes(steps):
    nodes = []
    for step in steps:
        a, b = step
        nodes.append(a)
        nodes.append(b)
    return set(nodes)


def detect_start(steps, nodes):
    start = [n for n in nodes if all(n != child for (_, child) in steps)]
    return sorted(start)


def process_steps(steps):
    step_order = ''
    nodes = unique_nodes(steps)
    while nodes:
        start = detect_start(steps, nodes)
        n = start.pop(0)
        step_order += n
        nodes.remove(n)
        steps = [(a, b) for (a, b) in steps if a != n]
    return step_order.upper()


assert process_steps(test_steps) == 'CABDFE'

part_one_answer = process_steps(steps)
assert part_one_answer == 'BGKDMJCNEQRSTUZWHYLPAFIVXO'
print('Part One:', part_one_answer)


def find_processing_time(step_time):
    node_values = {}
    for k, v in zip(ascii_lowercase, range(1, 27)):
        node_values[k] = v + step_time
    return node_values


def process_steps_workers(steps, workers=5, step_time=60, debug=False):
    step_order = ''
    nodes = unique_nodes(steps)
    node_values = find_processing_time(step_time)
    
    current_time = 0
    workers_busy = [0] * workers
    work_queue = [None] * workers
    
    while nodes or sum(workers_busy) > 0:
        start = detect_start(steps, nodes)
        for i in range(workers):
            
            # do one unit of work
            if workers_busy[i] > 0:
                workers_busy[i] -= 1
            
            if workers_busy[i] == 0:
                
                if work_queue[i] is not None:
                    # prep the queue for next round
                    steps = [(a, b) for (a, b) in steps if a != work_queue[i]]
                    # count any letter finished
                    if work_queue[i] not in step_order:
                        step_order += work_queue[i]
                
                # assign work if possible
                if len(start) > 0:
                    n = start.pop(0)
                    work_queue[i] = n
                    workers_busy[i] = node_values[n] - 1
                    nodes.remove(n)
            
        if debug:
            print(current_time, workers_busy, work_queue, step_order)
        current_time += 1
    return step_order.upper(), current_time


assert process_steps_workers(test_steps, workers=2, step_time=0) == ('CABFDE', 15)

part_two_answer = process_steps_workers(steps, workers=5, step_time=60)
print('Part Two:', part_two_answer[1])
