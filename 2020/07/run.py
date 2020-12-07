from aocd import get_data
from collections import defaultdict


def parse_line(line):
    bag, stuff = line.split(" bags contain ")
    other_bags = [s.strip() for s in stuff.replace(".", ",").split(",")]
    other_bags = [o for o in other_bags if len(o) > 0]
    if other_bags[0] == "no other bags":
        return {bag: 0}
    others = {}
    for o in other_bags:
        num, bag_type = o.split(" ", maxsplit=1)
        num = int(num)
        bag_type = bag_type.split(" bag")[0]
        others[bag_type] = num
    return {bag: others}


def parse_data(data):
    return data.splitlines()


def parse_bags(parsed_data):
    return [parse_line(d) for d in parsed_data]


def find_color(color, bags, parsed_data):
    found = [(i, d) for i, d in enumerate(parsed_data) if color in d and not d.startswith(color)]
    cols = []
    for i, f in found:
        bag = bags[i]
        cols += list(bag.keys())
    return cols


def find_all_colors(bags, parsed_data):
    seen = set(find_color("shiny gold", bags, parsed_data))
    new_seen = set()
    done = False
    while not done:
        for s in seen:
            new_seen.update(set(find_color(s, bags, parsed_data)))
        new_seen = new_seen - seen
        if len(new_seen) > 0:
            seen.update(new_seen)
        else:
            done = True
    return seen


def find_bags_in_shiny_gold(bags):
    bag_map = {}
    for b in bags:
        bag_map.update(b)
    count = defaultdict(int)
    ct = 0
    have = defaultdict(int)
    have['shiny gold'] = 1
    while len(have) > 0:
        col, amt = have.popitem()
        count[col] += amt
        try:
            for k, v in bag_map[col].items():
                have[k] += v*amt
                ct += v*amt 
        except:
            pass
    return count, ct
 

def solve_pt1(data):
    parsed_data = parse_data(data)
    bags = parse_bags(parsed_data)
    all_colors = find_all_colors(bags, parsed_data)
    return len(all_colors)


def solve_pt2(data):
    bags = parse_bags(data.splitlines())
    bags_counts, total = find_bags_in_shiny_gold(bags)
    return total


if __name__ == "__main__":
    data = get_data(year=2020, day=7)
    print("-" * 20, "Part 1:", "-" * 20)
    pt_1 = solve_pt1(data)
    print(pt_1, "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    pt_2 = solve_pt2(data)
    print(pt_2, "\n")
