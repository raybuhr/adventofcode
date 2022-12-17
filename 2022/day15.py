import sys
from dataclasses import dataclass


@dataclass
class Sensor:
    x: int
    y: int
    closest_beacon: tuple[int]
    distance: int


def manhattan_distance(a, b):
    return sum(abs(e1 - e2) for e1, e2 in zip(a, b))


def get_xy_coords(line):
    coord = line.split("x=")[-1].replace(" y=", "")
    coord = tuple([int(i) for i in coord.split(",")])
    return coord


def process_lines(lines):
    sensors, beacons = [], {}
    for line in lines:
        sensor, beacon = line.split(":")
        sensor, beacon = get_xy_coords(sensor), get_xy_coords(beacon)
        beacons[beacon] = 1
        sensors.append(
            Sensor(
                x=sensor[0],
                y=sensor[1],
                closest_beacon=beacon,
                distance=manhattan_distance(sensor, beacon),
            )
        )
    return sensors, beacons


def count_impossible_in_row(y):
    cant_have_beacon = {}

    for s in sensors:
        bx, by = s.closest_beacon
        b_dist = abs(s.x - bx) + abs(s.y - by)
        y_dist = abs(s.y - y)
        if y_dist <= b_dist:
            x_range = b_dist - y_dist
            for x in range(s.x - x_range, s.x + x_range + 1):
                if not beacons.get((x, y)):
                    cant_have_beacon[x] = True

    return len(cant_have_beacon)


def merge_intervals(intervals):
    # Sort the array on the basis of start values of intervals.
    intervals.sort()
    stack = []
    # insert first interval into stack
    stack.append(intervals[0])
    for i in intervals[1:]:
        # Check for overlapping interval
        if stack[-1][0] <= i[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], i[-1])
        else:
            stack.append(i)

    return stack


def find_sensor_range(sensor, y):
    v = abs(sensor.y - y)
    if v > sensor.distance:
        return [-1, -1]
    l = sensor.x - sensor.distance + v
    r = sensor.x + sensor.distance - v
    return [l, r]


def has_gaps(intervals, start=0, stop=4_000_000):
    for i in intervals:
        if i[0] > start:
            return True
        if i[1] < stop:
            return True
    return False


def check_rows(max_row):
    check_these_rows = {}
    for y in range(0, max_row + 1):
        m = merge_intervals([find_sensor_range(s, y) for s in sensors])
        if has_gaps(m, 0, max_row):
            check_these_rows[y] = m
    return check_these_rows


def find_beacon(max_row):
    rows = check_rows(max_row)
    for y, intervals in rows.items():
        if intervals[1][0] - 1 == intervals[0][1] + 1:
            x = intervals[1][0] - 1
            return x * max_row + y


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.read().strip().splitlines()

    sensors, beacons = process_lines(lines)
    row = 2_000_000
    impossible = count_impossible_in_row(row)
    print("part a:", impossible)
    freq = 4_000_000
    tuning_fequency = find_beacon(freq)
    print("part b:", tuning_fequency)
