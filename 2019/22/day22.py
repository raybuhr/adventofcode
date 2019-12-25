from aocd import get_data
import pytest


def parse_instruction(instruction):
    if "cut" in instruction:
        cmd, amt = instruction.split()
        return (cmd, int(amt))
    elif "deal with increment" in instruction:
        amt = instruction.split()[-1]
        return ("deal with increment", int(amt))
    elif "deal into new stack" in instruction:
        return ("deal into new stack", None)
    else:
        raise ValueError


def parse_data(data):
    return data.splitlines()


def shuffle_new_stack(cards, n=None):
    return cards[::-1]


def shuffle_cut(cards, n):
    top = cards[n:]
    bottom = cards[:n]
    return top + bottom


def shuffle_increment(cards, n):
    new_deck = [-1] * len(cards)
    length = len(new_deck)
    position = 0
    while cards:
        c = cards.pop(0)
        new_deck[position] = c
        position += n
        if position > length:
            position -= length
    return new_deck


def shuffle_cards(instruction, cards):
    shuffle_map = {
        "cut": shuffle_cut,
        "deal into new stack": shuffle_new_stack,
        "deal with increment": shuffle_increment,
    }
    command, amt = parse_instruction(instruction)
    return shuffle_map[command](cards, amt)


def shuffle_deck(instructions, cards):
    for instruction in instructions:
        cards = shuffle_cards(instruction, cards)
    return cards


def solve_part1(data):
    instructions = parse_data(data)
    cards = list(range(10007))
    deck = shuffle_deck(instructions, cards)
    return deck.index(2019)


def solve_part2(data):
    # https://www.reddit.com/r/adventofcode/comments/ee0rqi/2019_day_22_solutions/fbtugcu/?context=3
    cards = 119315717514047
    repeats = 101741582076661
    position = 2020
    deal_cut = lambda x, m, a, b: (a, (b - x) % m)
    deal_new = lambda _, m, a, b: (-a % m, (m - 1 - b) % m)
    deal_with_inc = lambda x, m, a, b: (a * x % m, b * x % m)
    shuffle_map = {
        "cut ": deal_cut,
        "deal into new stack": deal_new,
        "deal with increment ": deal_with_inc,
    }
    a, b = 1, 0
    for s in parse_data(data):
        for name, fn in shuffle_map.items():
            if s.startswith(name):
                arg = int(s[len(name) :]) if name[-1] == " " else 0
                a, b = fn(arg, cards, a, b)
                break
    r = (b * pow(1 - a, cards - 2, cards)) % cards
    return ((position - r) * pow(a, repeats * (cards - 2), cards) + r) % cards


def parse_test_result(cards_as_string):
    return list(map(int, cards_as_string.split()))


test_shuffle_cards_cases = [
    ("deal into new stack", list(range(10)), "9 8 7 6 5 4 3 2 1 0",),
    ("cut 3", list(range(10)), "3 4 5 6 7 8 9 0 1 2"),
    ("cut -4", list(range(10)), "6 7 8 9 0 1 2 3 4 5"),
    ("deal with increment 3", list(range(10)), "0 7 4 1 8 5 2 9 6 3"),
]


@pytest.mark.parametrize("instruction,cards,expected", test_shuffle_cards_cases)
def test_shuffle_cards(instruction, cards, expected):
    assert shuffle_cards(instruction, cards) == parse_test_result(expected)


test_shuffle_deck_cases = [
    (
        """deal with increment 7
deal into new stack
deal into new stack""",
        list(range(10)),
        "0 3 6 9 2 5 8 1 4 7",
    ),
    (
        """cut 6
deal with increment 7
deal into new stack""",
        list(range(10)),
        "3 0 7 4 1 8 5 2 9 6",
    ),
    (
        """deal with increment 7
deal with increment 9
cut -2""",
        list(range(10)),
        "6 3 0 7 4 1 8 5 2 9",
    ),
    (
        """deal into new stack
cut -2
deal with increment 7
cut 8
cut -4
deal with increment 7
cut 3
deal with increment 9
deal with increment 3
cut -1""",
        list(range(10)),
        "9 2 5 8 1 4 7 0 3 6",
    ),
]


@pytest.mark.parametrize("instructions,cards,expected", test_shuffle_deck_cases)
def test_shuffle_deck(instructions, cards, expected):
    instructions = parse_data(instructions)
    assert shuffle_deck(instructions, cards) == parse_test_result(expected)


if __name__ == "__main__":
    data = get_data(year=2019, day=22)

    print("-" * 20, "Part 1:", "-" * 20)
    print(solve_part1(data), "\n")

    print("-" * 20, "Part 2:", "-" * 20)
    print(solve_part2(data), "\n")
