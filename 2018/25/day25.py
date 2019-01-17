from string import ascii_letters
from collections import Counter


with open('data.txt') as f:
    data = f.read().splitlines()


def manh_dist(a, b):
    lengths = []
    for i in range(len(a)):
        lengths.append(abs(a[i]-b[i]))
    return sum(lengths)


def convert_string_to_point(point_as_string):
    return [int(x) for x in point_as_string.split(',')]


def in_same_constellation(a, b):
    if type(a) is str:
        a = convert_string_to_point(a)
    if type(b) is str:
        b = convert_string_to_point(b)
    dist = manh_dist(a, b)
    if dist <= 3:
        return True
    return False


def find_constellations(list_of_points):
    letters = list(ascii_letters)
    current_letter = letters.pop(0)
    current_point = list_of_points.pop(0)
    constellations = {}
    constellations[current_point] = current_letter
    # initialize constellations
    for point in list_of_points:
        if in_same_constellation(current_point, point):
            constellations[point] = current_letter
            list_of_points.remove(point)
    # go through remaining
    while list_of_points:
        current_list_length = len(list_of_points)
        for point in list_of_points:
            found = [k for k in constellations.keys()
                    if constellations.get(k) == current_letter]
            for pt in found:
                if in_same_constellation(point, pt):
                    constellations[point] = current_letter
                    list_of_points.remove(point)

        # check if that loop did anything
        # if yes, do it again
        # if no, move on to new letter
        if len(list_of_points) == current_list_length:
            current_letter = letters.pop(0)
            current_point = list_of_points.pop(0)
            constellations[current_point] = current_letter
    return constellations


def count_constellations(constellations):
    counts = Counter(constellations.values())
    return len(counts)


def answer_part_one(data):
    constellations = find_constellations(data)
    count = count_constellations(constellations)
    print(count)
    return constellations


