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
    sensors, beacons = [], []
    for line in lines:
        sensor, beacon = line.split(":")
        sensor, beacon = get_xy_coords(sensor), get_xy_coords(beacon)
        beacons.append(beacon)
        sensors.append(
            Sensor(
                x=sensor[0],
                y=sensor[1],
                closest_beacon=beacon,
                distance=manhattan_distance(sensor, beacon),
            )
        )
    return sensors, beacons


def can_point_contain_a_beacon(x, y, sensor):
    d = manhattan_distance((sensor.x, sensor.y), (x, y))
    if d <= sensor.distance:
        return False
    return (x, y) in beacons


def find_impossible_in_row(y, start, stop):
    ct = 0
    for x in range(start, stop+1):
        if not any(can_point_contain_a_beacon(x, y, s) for s in sensors):
             ct += 1
    return ct


if __name__ == "__main__":
    with open(sys.argv[1]) as f:
        lines = f.read().strip().splitlines()

    sensors, beacons = process_lines(lines)
    print("Sensors:")
    for s in sensors:
        print(s)
