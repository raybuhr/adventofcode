def check_if_triangle(sides):
    sides = [int(s) for s in sides]
    a, b, c = sides
    ab = a + b
    ac = a + c
    bc = b + c
    return all([ab > c, ac > b, bc > a])


def test_check_if_triangle():
    assert check_if_triangle([5, 10, 25]) is False
    assert check_if_triangle([5, 6, 7]) is True


def solve_part_1(data):
    is_triangle = [
        check_if_triangle(sides)
        for sides in data
    ]
    return sum(is_triangle)


def split_data_into_columns(data):
    triangles = []
    num_columns = len(data[0])
    for col in range(num_columns):
        column = [line[col] for line in data]
        for i in range(0, len(column), 3):
            triangles.append(column[i:(i+3)])
    return triangles


def solve_part_2(data):
    triangles = split_data_into_columns(data)
    is_triangle = [
        check_if_triangle(sides)
        for sides in triangles
    ]
    return sum(is_triangle)


if __name__ == "__main__":
    with open('input.txt') as fp:
        data = [
            line.split()
            for line in
            fp.read().split("\n")
        ]
    
    print("Part 1:")
    pt1 = solve_part_1(data)
    print(pt1)
    
    print("Part 2:")
    pt2 = solve_part_2(data)
    print(pt2)
