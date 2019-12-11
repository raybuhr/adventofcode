from aocd import get_data


def parse_data(data):
    out = data.splitlines()
    return out


def parse_orbits(data):
    return {b: a for a, b in [d.split(")") for d in data]}


def find_orbits(obj, orbits):
    objs = []
    o = obj
    done = False
    while not done:
        r = orbits.get(o)
        if r is not None:
            objs.append(r)
            o = r
        else:
            done = True
    return objs


def count_orbits(orbits):
    all_orbits = {o: find_orbits(o, orbits) for o in orbits}
    return sum(len(v) for v in all_orbits.values())


def test_find_orbits():
    test_data = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""
    test_orbits = parse_orbits(parse_data(test_data))
    assert count_orbits(test_orbits) == 42


def find_distance_between_objects(a, b, orbits):
    path_a = find_orbits(a, orbits)
    path_b = find_orbits(b, orbits)
    uniq_a = [i for i in path_a if i not in path_b]
    uniq_b = [i for i in path_b if i not in path_a]
    return len(uniq_a + uniq_b)


def test_find_distance_between_objects():
    test_data = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN"""
    test_orbits = parse_orbits(parse_data(test_data))
    assert find_distance_between_objects("SAN", "YOU", test_orbits) == 4


def solve_part1():
    orbits = parse_orbits(parse_data(read_data()))
    output = count_orbits(orbits)
    print(output)


def solve_part2():
    orbits = parse_orbits(parse_data(read_data()))
    dist = find_distance_between_objects("YOU", "SAN", orbits)
    print(dist)


if __name__ == "__main__":
    data = get_data(year=2019, day=6)
    print("Part 1:")
    solve_part1()

    print("Part 2:")
    solve_part2()
