from aocd import get_data


def parse_data(data):
    return [parse_pw_policy(i) for i in data.splitlines()]


def parse_pw_policy(policy):
    times, letter, pw = policy.split(" ")
    min_times, max_times = times.split("-")
    letter = letter.replace(":", "")
    return (int(min_times), int(max_times), letter, pw)


def is_valid_password(min_times, max_times, letter, pw):
    times = 0
    for l in pw:
        if l == letter:
            times += 1
    if times >= min_times and times <= max_times:
        return True
    return False


def solve_pt1(data):
    passwords = parse_data(data)
    return sum(is_valid_password(*pw) for pw in passwords)


def solve_pt2(data):
    passwords = parse_data(data)
    num_valid = 0
    for pw in passwords:
        pos1, pos2 = pw[0]-1, pw[1]-1
        letter, password = pw[2], pw[3]
        if (password[pos1] == letter) ^ (password[pos2] == letter):
            num_valid += 1
    return num_valid


if __name__ == "__main__":
    data = get_data(year=2020, day=2)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_pt1(data)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")

