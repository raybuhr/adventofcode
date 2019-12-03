def parse_data(data):
    instructions = [
    	(i[0], int(i[1:]))
	for i in data.split(",")
    ]
    return instructions


def manhattan_distance(x, y):
    return abs(x) + abs(y)


def find_min_dist(points):
   return min(manhattan_distance(pt[0], pt[1]) for pt in points)


def track_path(instructions):
    x, y = 0, 0
    points = []
    for instruction in instructions:
        direction, dist = instruction
        if direction == "U":
            new_pts = [(x, y + i) for i in range(1, dist+1)]
            points += new_pts
            y = y + dist
        if direction == "D":
            new_pts = [(x, y - i) for i in range(1, dist+1)]
            points += new_pts
            y = y - dist
        if direction == "R":
            new_pts = [(x + i, y) for i in range(1, dist+1)]
            points += new_pts
            x = x + dist
        if direction == "L":
            new_pts = [(x - i, y) for i in range(1, dist+1)]
            points += new_pts
            x = x - dist
    return points


def find_intersections(path1, path2):
    a = set(path1)
    b = set(path2)
    return a.intersection(b)


def test_find_min_dist():
    paths = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"
    expect = 159
    a, b = paths.split("\n")
    a, b = parse_data(a), parse_data(b)
    a, b = track_path(a), track_path(b)
    same_points = find_intersections(a, b)
    got = find_min_dist(same_points)
    assert expect == got
    paths = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    expect = 135
    a, b = paths.split("\n")
    a, b = parse_data(a), parse_data(b)
    a, b = track_path(a), track_path(b)
    same_points = find_intersections(a, b)
    got = find_min_dist(same_points)
    assert expect == got


def solve_pt1(data):
    a, b = data.split("\n")
    a, b = parse_data(a), parse_data(b)
    a, b = track_path(a), track_path(b)
    same_points = find_intersections(a, b)
    got = find_min_dist(same_points)
    return got


def find_min_latency(path1, path2):
    same_points = find_intersections(path1, path2)
    point_steps = []
    for pt in same_points:
        a = path1.index(pt) + 1
        b = path2.index(pt) + 1
        steps = a + b
        point_steps.append(steps)
    return min(point_steps)


def test_find_min_latency():
    paths = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83"
    expect = 610
    a, b = paths.split("\n")
    a, b = parse_data(a), parse_data(b)
    a, b = track_path(a), track_path(b)
    got = find_min_latency(a, b)
    assert expect == got
    paths = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    expect = 410
    a, b = paths.split("\n")
    a, b = parse_data(a), parse_data(b)
    a, b = track_path(a), track_path(b)
    got = find_min_latency(a, b)
    assert expect == got


def solve_pt2(data):
    a, b = data.split("\n")
    a, b = parse_data(a), parse_data(b)
    a, b = track_path(a), track_path(b)
    got = find_min_latency(a, b)
    return got


if __name__ == "__main__":
    with open("2019/03/input.txt") as fp:
        data = fp.read().strip()

    print("Part 1:")
    print(solve_pt1(data))

    print("Part 2:")
    print(solve_pt2(data))

