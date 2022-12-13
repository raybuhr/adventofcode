from collections import defaultdict
from functools import reduce

with open("input.txt") as f:
    lines = [line.splitlines() for line in f.read().split("\n\n")]


test_lines = [
    line.splitlines()
    for line in """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".split(
        "\n\n"
    )
]


def parse_monkey(monkey):
    id_ = int(monkey[0].replace(":", "").replace("Monkey ", ""))
    items = [
        int(i) for i in monkey[1].strip().replace("Starting items: ", "").split(", ")
    ]

    cmd = monkey[2].strip().replace("Operation: new = ", "")

    def operation(old):
        new = eval(cmd)
        return new

    div_ = int(monkey[3].strip().replace("Test: divisible by ", ""))
    a = int(monkey[4].strip().replace("If true: throw to monkey ", ""))
    b = int(monkey[5].strip().replace("If false: throw to monkey ", ""))

    def test(x):
        check = lambda x: x % div_ == 0
        if check(x):
            return a
        else:
            return b

    return {
        id_: {"items": items, "operation": operation, "test": test, "divisible": div_}
    }


def step(monkey, part="a"):
    try:
        worry = monkey["items"].pop(0)
        worry = monkey["operation"](worry)
        if part == "a":
            worry = worry // 3
        # else:
        #     worry = worry % monkey["divisible"]
        send_to = monkey["test"](worry)
        return send_to, worry
    except:
        return None, None


def run_round(monkeys, part="a"):
    i = 0
    inspections = defaultdict(int)
    divisor = reduce(lambda x, y: x * y, [monkeys[m]["divisible"] for m in monkeys])
    for m in monkeys.keys():
        items = monkeys[m]["items"]
        monkeys[m]["items"] = [i % divisor for i in items]
    while i in monkeys:
        monkey = monkeys[i]
        send_to, worry = step(monkey, part)
        if send_to is not None:
            # print(f"item with worry {worry} thrown to monkey {send_to}")
            inspections[i] += 1
            monkeys[send_to]["items"].append(worry)
        else:
            # print(f"no item to send, next monkey is {i+1}")
            i += 1
    return inspections


def init_monkeys(lines):
    monkeys = {}
    for line in lines:
        monkeys.update(parse_monkey(line))
    return monkeys


def run_rounds(monkeys, part, rounds, verbose=False):
    inspections = defaultdict(int)
    while rounds:
        round_inspections = run_round(monkeys, part)
        for monkey, count in round_inspections.items():
            inspections[monkey] += count
        rounds -= 1
    if verbose:
        print(monkeys)
    return inspections


def solve(lines, part):
    rounds = 20 if part == "a" else 10_000
    monkeys = init_monkeys(lines)
    inspections = run_rounds(monkeys, part, rounds)
    return reduce(lambda x, y: x * y, sorted(inspections.values(), reverse=True)[:2])


if __name__ == "__main__":
    print("part a:", solve(lines, "a"))
    print("part b:", solve(lines, "b"))
