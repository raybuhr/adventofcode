def read_data():
    with open("2018/13/data.txt") as fp:
        data = fp.read().strip()
    return data


def parse_data(data):
    rows = data.splitlines()
    mine = [[col for col in row] for row in rows]
    return mine


def find_carts(mine):
    """up (^), down (v), left (<), or right (>)"""
    carts = {}
    counter = 0
    for r, row in enumerate(mine):
        for c, col in enumerate(row):
            if col in ("^", "v", "<", ">"):
                carts[counter] = {
                        "direction": col,
                        "position": (r, c),
                        "turn": 0,
                        }
                counter += 1
    return carts


def clear_carts_from_mine(mine):
    for r, row in enumerate(mine):
        for c, col in enumerate(row):
            if col in ("^", "v"):
                mine[r][c] = "|"
            if col in ("<", ">"):
                mine[r][c] = "-"


def step(mine, carts):
    moves = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
    }
    directions = {
        "|": 0,
        "-": 0,
        "\\": 1,
        "/": 1,
        "+": 1,
    }
    turns = {
        0: {">": "^", "v": ">", "<": "v", "^": "<"},
        1: {">": ">", "v": "v", "<": "<", "^": "^"},
        2: {">": "v", "v": "<", "<": "^", "^": ">"},
    }
    for i, cart in carts.items():
        row, col = moves[cart["direction"]]
        cur_position = cart["position"]
        new_position = (cur_position[0] + row, cur_position[1] + col)
        cart["position"] = new_position
        next_direction = mine[new_position[0]][new_position[1]]
        change_dir = directions[next_direction]
        if change_dir:
            cur_direction = cart["direction"]
            if next_direction == "+":
                turn = cart["turn"] % 3
                new_direction = turns[turn][cur_direction]
                cart["turn"] += 1
            if next_direction == "/":
                if cur_direction == "^":
                    new_direction = ">"
                if cur_direction == "v":
                    new_direction = "<"
                if cur_direction == ">":
                    new_direction = "^"
                if cur_direction == "<":
                    new_direction = "v"
            if next_direction == "\\":
                if cur_direction == "^":
                    new_direction = "<"
                if cur_direction == "v":
                    new_direction = ">"
                if cur_direction == ">":
                    new_direction = "v"
                if cur_direction == "<":
                    new_direction = "^"
            cart["direction"] = new_direction


def check_for_crash(carts):
    positions = [cart["position"] for cart in carts.values()]
    uniq = {p: 0 for p in positions}
    if len(positions) > len(uniq):
        for p in positions:
            uniq[p] += 1
        return [u for u, v in uniq.items() if v > 1]
    return False


def test_solve_part1():
    test_data = """/->-\        
|   |  /----\ 
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   """
    mine = parse_data(test_data)
    carts = find_carts(mine)
    clear_carts_from_mine(mine)
    done = False
    steps = 1
    while not done:
        step(mine, carts)
        crash = check_for_crash(carts)
        if crash:
            done = True
        steps += 1
    first_crash = min(c for c in crash)
    coords = (first_crash[1], first_crash[0])
    assert coords == (7, 3)


def solve_part1():
    data = read_data()
    mine = parse_data(data)
    carts = find_carts(mine)
    clear_carts_from_mine(mine)
    done = False
    steps = 1
    while not done:
        step(mine, carts)
        crash = check_for_crash(carts)
        if crash:
            done = True
        steps += 1
    first_crash = min(c for c in crash)
    coords = (first_crash[1], first_crash[0])
    return coords


def solve_part2():
    pass


if __name__ == "__main__":
    print("Part 1:")
    solve_part1()
    print("")
    print("Part 2:")
    solve_part2()
