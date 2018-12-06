#!/usr/bin/env python
# coding: utf-8

from collections import defaultdict, Counter
from typing import List, Set, Tuple
# from scipy.spatial.distance import cityblock as manhattan_dist # this is SLOW AF

with open('data.txt') as datafile:
    data = datafile.read().split('\n')

test_case = [
    '1, 1',
    '1, 6',
    '8, 3',
    '3, 4',
    '5, 5',
    '8, 9',
]

def convert_text_to_coordiates(coord_text):
    '''
    convert list of something like "1, 1" to set of (1, 1)
    
    return: 
    set of tupule x, y points
    max x
    max y
    '''
    coords = set()
    max_x, max_y = 0, 0
    for text in coord_text:
        x, y = map(int, text.split(','))
        coords.add((x, y))
        if x > max_x: max_x = x
        if y > max_y: max_y = y
    return {'coordinates': coords, 'max_x': max_x, 'max_y': max_y}


def manhattan_dist(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


def find_closest_points(point: tuple, coordinates: set) -> list :
    points = []
    min_dist = 99999999
    for coord in coordinates:
        pt_dist = manhattan_dist(point, coord)
        # add tied min distance points
        if pt_dist == min_dist:
            min_dist = pt_dist
            points.append(coord)
        # new min distance
        if pt_dist < min_dist:
            min_dist = pt_dist
            points.clear()
            points.append(coord)
    if len(points) == 1:
        point = points[0]
        return point
    return None


def define_edges(max_x: int, max_y: int):
    bottom_edge = [(x, 0) for x in range(max_x+1)]
    top_edge = [(x, max_y) for x in range(max_x+1)]
    left_edge = [(0, y) for y in range(max_y+1)]
    right_edge = [(max_x, y) for y in range(max_y+1)]
    edges = bottom_edge + top_edge + left_edge + right_edge
    return set(edges)


def count_areas(coordinates):
    coords = coordinates.get('coordinates')
    max_x = coordinates.get('max_x')
    max_y = coordinates.get('max_y')
    area_counts = defaultdict(float)
    edges = define_edges(max_x, max_y)
    for x in range(max_x+1):
        for y in range(max_y+1):
            closest_point = (find_closest_points((x, y), coords))
            if (x, y) in edges:
                area_counts[closest_point] += float('inf')
            else:
                area_counts[closest_point] += 1
    return area_counts


def part_one_answer(raw_data):
    coords = convert_text_to_coordiates(raw_data)
    area_counts = count_areas(coords)
    max_area = max([a for a in area_counts.values() if a != float('inf')])
    return max_area

def part_two_answer(raw_data, min_dist):
    coordinates = convert_text_to_coordiates(raw_data)
    coords = coordinates.get('coordinates')
    max_x = coordinates.get('max_x')
    max_y = coordinates.get('max_y')
    keep = set()
    for x in range(max_x+1):
        for y in range(max_y+1):
            point_dist = []
            for c in coords:
                point_dist.append(manhattan_dist((x, y), c))
            if sum(point_dist) < min_dist:
                keep.add((x, y))
    return len(keep)

if __name__ == '__main__':
    assert part_one_answer(test_case) == 17
    assert part_two_answer(test_case, 32) == 16
    
    print('Part One:', part_one_answer(data))
    print('Part Two:', part_two_answer(data, 10000))
