from aocd import get_data
from dataclasses import dataclass


@dataclass
class CrabCups:
    cups: list
    label: int
    pickup = []
    moves = 0

    def move(self):
        self.moves += 1
        idx = self.cups.index(self.label)
        while len(self.pickup) < 3:
            if len(self.cups) > idx + 1:
                self.pickup += [self.cups.pop(idx + 1)]
            else:
                self.pickup += [self.cups.pop(0)]
        dest = False
        label = self.label
        while not dest:
            dest = label - 1
            if dest < 1:
                dest = max(self.cups)
            if dest in self.pickup:
                dest = False
                label -= 1
        dest = self.cups.index(dest)
        while self.pickup:
            p = self.pickup.pop()
            self.cups.insert(dest+1, p)
        new_idx = self.cups.index(self.label) + 1
        self.label = self.cups[new_idx % len(self.cups)]

    def get_order(self):
        order = self.cups[self.cups.index(1)+1:] + self.cups[:self.cups.index(1)]
        return ''.join([str(o) for o in order])


def move_cup(at, cups):
    a = cups[at]
    b = cups[a]
    c = cups[b]
    dest = at - 1
    if dest <= 0:
        dest = len(cups)
    while dest in [a, b, c]:
        dest -= 1
        if dest <= 0:
            dest = len(cups)
    d = cups[dest]
    cups[at] = cups[c]
    cups[dest] = a
    cups[c] = d
    return cups[at]

    
def solve_part_a(data):
    cups = [int(c) for c in data]
    game = CrabCups(cups=cups, label=cups[0])
    for _ in range(100):
        game.move()
    return game.get_order()


def solve_part_b(data):
    cups = [int(c) for c in data] + list(range(10, 1_000_001))
    cups = {n: r for n, r in zip(cups, cups[1:] + cups[:1])}
    at = int(data[0])
    for step in range(10_000_000):
        at = move_cup(at, cups)        
    a = cups[1]
    b = cups[a]
    return a * b


if __name__ == "__main__":
    data = get_data(year=2020, day=23)
    print("-"*40)
    print("Part 1:")
    a = solve_part_a(data)
    print(a)
    print("-"*40)
    print("Part 2:")
    b = solve_part_b(data)
    print(b)

