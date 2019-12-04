from collections import Counter

def parse_data_range(data):
    start, stop = [int(d) for d in data.split("-")]
    return range(start, stop + 1)


def has_two_adjacent_numbers(password):
    shifted = password[1:] + " "
    return any(password[i] == shifted[i] for i in range(6))


def is_increasing(password):
    return all(password[i] >= password[i - 1] for i in range(1, 6))


def is_valid_password(password):
    return all([has_two_adjacent_numbers(password), is_increasing(password)])


def test_is_valid_password():
    assert is_valid_password("111111") is True
    assert is_valid_password("223450") is False
    assert is_valid_password("123789") is False


def is_super_valid_password(password):
    if not is_increasing(password):
        return False
    counter = Counter(password)
    return any(c == 2 for c in counter.values())


def test_is_super_valid_password():
    assert is_super_valid_password("112233") is True
    assert is_super_valid_password("123444") is False
    assert is_super_valid_password("111122") is True


if __name__ == "__main__":
    data = "246540-787419"
    data_range = parse_data_range(data)
    print("Part 1:")
    pt1 = sum(is_valid_password(str(d)) for d in data_range)
    print(pt1)

    print("Part 2:")
    pt2 = sum(is_super_valid_password(str(d)) for d in data_range)
    print(pt2)
